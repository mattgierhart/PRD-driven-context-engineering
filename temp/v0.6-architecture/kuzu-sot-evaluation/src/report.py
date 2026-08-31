"""Self-contained HTML renderer for the Kuzu-vs-Markdown benchmark."""

from __future__ import annotations

import html
import json
from collections import defaultdict
from typing import Any


DISPLAY_NAMES = {
    "heartbeat": "HeartBeat",
    "agenthunt": "AgentHunt",
    "homefalcon": "HomeFalcon",
    "prd-ce": "PRD-CE template",
}


def escape(value: Any) -> str:
    return html.escape(str(value), quote=True)


def fmt_number(value: float | int, digits: int = 1) -> str:
    if isinstance(value, int):
        return f"{value:,}"
    return f"{value:,.{digits}f}"


def fmt_bytes(value: int | float) -> str:
    amount = float(value)
    for unit in ("B", "KB", "MB", "GB"):
        if abs(amount) < 1024 or unit == "GB":
            digits = 0 if unit == "B" else 1
            return f"{amount:,.{digits}f} {unit}"
        amount /= 1024
    return f"{amount:,.1f} GB"


def fmt_ms(value: float) -> str:
    if value < 1:
        return f"{value * 1000:,.0f} μs"
    if value < 1000:
        return f"{value:,.2f} ms"
    return f"{value / 1000:,.2f} s"


def bar_row(label: str, value: float, maximum: float, display: str, kind: str) -> str:
    width = 0 if maximum <= 0 else max(2, min(100, value / maximum * 100))
    return f"""
      <div class="bar-row">
        <div class="bar-label">{escape(label)}</div>
        <div class="bar-track"><span class="bar-fill {escape(kind)}" style="width:{width:.2f}%"></span></div>
        <div class="bar-value">{escape(display)}</div>
      </div>"""


def render_corpus_table(corpora: list[dict[str, Any]]) -> str:
    rows = []
    for corpus in corpora:
        rows.append(
            f"""
            <tr>
              <td><strong>{escape(DISPLAY_NAMES.get(corpus['alias'], corpus['alias']))}</strong>
                  <span class="hash">{escape(corpus['fingerprint_sha256'][:10])}</span></td>
              <td>{corpus['files']:,}</td>
              <td>{corpus['defined_nodes']:,}</td>
              <td>{corpus['edges']:,}</td>
              <td>{corpus['dangling_nodes']:,}</td>
              <td>{fmt_ms(corpus['parse_ms'])}</td>
              <td>{fmt_ms(corpus['kuzu_build_ms'])}</td>
              <td>{fmt_bytes(corpus['source_bytes'])}</td>
              <td>{fmt_bytes(corpus['kuzu_database_bytes'])}</td>
            </tr>"""
        )
    return "".join(rows)


def render_build_chart(corpora: list[dict[str, Any]]) -> str:
    maximum = max(
        (
            max(corpus["parse_ms"], corpus["kuzu_build_ms"])
            for corpus in corpora
        ),
        default=1,
    )
    rows = []
    for corpus in corpora:
        name = DISPLAY_NAMES.get(corpus["alias"], corpus["alias"])
        rows.append(
            f'<div class="chart-group"><p>{escape(name)}</p>'
            + bar_row(
                "Markdown parse",
                corpus["parse_ms"],
                maximum,
                fmt_ms(corpus["parse_ms"]),
                "markdown",
            )
            + bar_row(
                "Kuzu materialize",
                corpus["kuzu_build_ms"],
                maximum,
                fmt_ms(corpus["kuzu_build_ms"]),
                "kuzu",
            )
            + "</div>"
        )
    return "".join(rows)


def render_storage_chart(corpora: list[dict[str, Any]]) -> str:
    maximum = max(
        (
            max(corpus["source_bytes"], corpus["kuzu_database_bytes"])
            for corpus in corpora
        ),
        default=1,
    )
    rows = []
    for corpus in corpora:
        name = DISPLAY_NAMES.get(corpus["alias"], corpus["alias"])
        rows.append(
            f'<div class="chart-group"><p>{escape(name)}</p>'
            + bar_row(
                "Markdown source",
                corpus["source_bytes"],
                maximum,
                fmt_bytes(corpus["source_bytes"]),
                "markdown",
            )
            + bar_row(
                "Kuzu database",
                corpus["kuzu_database_bytes"],
                maximum,
                fmt_bytes(corpus["kuzu_database_bytes"]),
                "kuzu",
            )
            + "</div>"
        )
    return "".join(rows)


def render_query_chart(rollup: dict[str, Any]) -> str:
    maximum = max(
        (metrics["median_query_ms"] for metrics in rollup.values()),
        default=1,
    )
    return "".join(
        bar_row(
            "Markdown in-memory" if engine == "markdown" else "Kuzu embedded",
            metrics["median_query_ms"],
            maximum,
            fmt_ms(metrics["median_query_ms"]),
            engine,
        )
        for engine, metrics in rollup.items()
    )


def render_case_rows(cases: list[dict[str, Any]]) -> str:
    paired: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for row in cases:
        paired[row["case_id"]][row["engine"]] = row
    rendered = []
    for case_id, engines in paired.items():
        markdown = engines["markdown"]
        graph = engines["kuzu"]
        exact = markdown["exact"] and graph["exact"]
        result_ids = ", ".join(markdown["actual"]) or "∅"
        rendered.append(
            f"""
            <tr data-corpus="{escape(markdown['corpus'])}"
                data-kind="{escape(markdown['kind'])}"
                data-status="{'pass' if exact else 'fail'}">
              <td>
                <span class="case-id">{escape(case_id)}</span>
                <strong>{escape(markdown['question'])}</strong>
              </td>
              <td>{escape(DISPLAY_NAMES.get(markdown['corpus'], markdown['corpus']))}</td>
              <td><span class="badge {'pass' if markdown['exact'] else 'fail'}">
                {'exact' if markdown['exact'] else 'miss'}
              </span><br><span class="latency">{fmt_ms(markdown['latency_ms']['median'])}</span></td>
              <td><span class="badge {'pass' if graph['exact'] else 'fail'}">
                {'exact' if graph['exact'] else 'miss'}
              </span><br><span class="latency">{fmt_ms(graph['latency_ms']['median'])}</span></td>
              <td><code>{escape(result_ids)}</code></td>
            </tr>"""
        )
    return "".join(rendered)


def render_payload_chart(rollup: dict[str, Any]) -> str:
    markdown = rollup["markdown"]
    values = {
        "Whole source files": markdown["median_whole_file_bytes"],
        "Exact Markdown entries": markdown["median_exact_entry_bytes"],
        "Structured projection": markdown["median_projection_bytes"],
    }
    maximum = max(values.values()) or 1
    kinds = ("files", "markdown", "projection")
    return "".join(
        bar_row(label, value, maximum, fmt_bytes(value), kind)
        for (label, value), kind in zip(values.items(), kinds)
    )


def render_semantic_rows(checks: list[dict[str, Any]]) -> str:
    if not checks:
        return (
            '<tr><td colspan="5">No deterministic semantic checks were '
            "included in this result schema.</td></tr>"
        )
    rows = []
    for check in checks:
        findings = ", ".join(
            finding["code"] for finding in check.get("findings", ())
        ) or "none"
        exact = check.get("verdict_exact", False)
        rows.append(
            f"""
            <tr>
              <td><code>{escape(check['case_id'])}</code></td>
              <td>{escape(check.get('lifecycle_stage') or '—')}</td>
              <td>{escape(check.get('expected_verdict', '—'))}</td>
              <td><span class="badge {'pass' if exact else 'fail'}">
                {escape(check.get('actual_verdict', '—'))}
              </span></td>
              <td><code>{escape(findings)}</code></td>
            </tr>"""
        )
    return "".join(rows)


def render_report(data: dict[str, Any]) -> str:
    rollup = data["rollup"]
    corpora = data["corpora"]
    markdown = rollup["markdown"]
    graph = rollup["kuzu"]
    authority = data["authority_boundary"]
    total_nodes = sum(corpus["defined_nodes"] for corpus in corpora)
    total_files = sum(corpus["files"] for corpus in corpora)
    total_cases = markdown["cases"]
    accuracy = data.get("accuracy_dimensions", {})
    semantic = accuracy.get("semantic_truth", {})
    semantic_checks = semantic.get("checks", [])
    semantic_assessed = semantic.get("assessed_cases", 0)
    semantic_exact = semantic.get("verdict_exact_cases", 0)
    lifecycle = accuracy.get("lifecycle_manifest_coverage", {})
    lifecycle_expected = lifecycle.get("expected_stages", [])
    lifecycle_covered = lifecycle.get("covered_stages", [])
    all_exact = markdown["exact_rate"] == 1 and graph["exact_rate"] == 1
    acceptance = data.get("acceptance", {})
    accepted = acceptance.get("passed") is True
    source_fidelity_accepted = (
        acceptance.get("checks", {})
        .get("source_fidelity", {})
        .get("passed")
        is True
    )
    measured_decision = data.get("decision", {}).get(
        "measured",
        "No measured decision was recorded.",
    )
    hero_title = (
        "Markdown wins this round."
        if accepted
        else "Benchmark acceptance failed."
    )
    hero_summary = (
        f"Across {total_cases} manifest-authored source-fidelity cases, "
        "Markdown and Kuzu reproduced the same authored IDs—but structural "
        "fidelity is not semantic truth. The in-memory Markdown index remained "
        "faster, while deterministic semantic checks correctly flagged "
        "authored defects."
        if accepted
        else "The run persisted its evidence, but at least one required "
        "source-fidelity, semantic, lifecycle-manifest, or authority check "
        "failed. Treat every architecture conclusion below as withheld until "
        "the acceptance findings are resolved."
    )
    verdict_title = (
        "Keep Markdown as the SoT."
        if accepted
        else "Withhold the architecture decision."
    )
    verdict_summary = (
        "Kuzu proves graph materialization is feasible. It does not yet prove "
        "enough incremental value to justify a production graph layer—and its "
        "archived status rules it out as the default engine."
        if accepted
        else measured_decision
    )
    decision_heading = (
        "Markdown wins the measured jobs; graph value remains conditional."
        if accepted
        else "No decision passes the evidence gate."
    )
    current_scope_title = (
        "Markdown + ephemeral index"
        if accepted
        else "Architecture decision withheld"
    )
    current_scope_summary = (
        "Portable, diffable, reviewable, and agent-readable. The shared parser "
        "plus an in-memory adjacency map answered every tested lookup, reverse, "
        "and multi-hop case with the lowest measured cost."
        if accepted
        else "The evidence remains inspectable, but the acceptance policy "
        "requires every check to pass before naming a measured winner."
    )
    query_winner = (
        "Markdown in-memory"
        if markdown["median_query_ms"] <= graph["median_query_ms"]
        else "Kuzu"
    )
    aggregate_storage_ratio = sum(
        corpus["kuzu_database_bytes"] for corpus in corpora
    ) / sum(corpus["source_bytes"] for corpus in corpora)
    storage_ratios = [
        corpus["database_to_markdown_size_ratio"] for corpus in corpora
    ]
    generated = data["generated_at"].split("T", 1)[0]
    embedded_data = json.dumps(
        data, separators=(",", ":"), sort_keys=True
    ).replace("</", "<\\/")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Kuzu vs Markdown · PRD-CE SoT Evaluation</title>
  <style>
    :root {{
      --paper:#f3efe4; --sheet:#fbf8ef; --ink:#171510; --muted:#6b665b;
      --line:#d6cfbf; --gold:#a77f23; --gold-soft:#eee3c5;
      --green:#38623a; --green-soft:#e0eadc; --red:#9a3c2f; --red-soft:#f1ddd8;
      --blue:#315b70; --blue-soft:#dce8eb; --purple:#62506d;
      --serif:"Iowan Old Style","Palatino Linotype",Georgia,serif;
      --sans:"Helvetica Neue",Helvetica,Arial,sans-serif;
      --mono:"SFMono-Regular",Consolas,"Liberation Mono",monospace;
    }}
    * {{ box-sizing:border-box; }}
    html {{ scroll-behavior:smooth; }}
    body {{
      margin:0; color:var(--ink); background:
        radial-gradient(circle at 11% 0%, rgba(167,127,35,.08), transparent 24rem),
        var(--paper); font-family:var(--serif); line-height:1.55;
    }}
    a {{ color:inherit; text-decoration-color:var(--gold); text-underline-offset:3px; }}
    .topbar {{
      position:sticky; top:0; z-index:20; display:flex; align-items:center; gap:20px;
      padding:12px max(22px, calc((100vw - 1180px)/2)); background:rgba(243,239,228,.95);
      backdrop-filter:blur(10px); border-top:6px solid var(--ink); border-bottom:1px solid var(--ink);
      font:700 10px/1 var(--sans); letter-spacing:.14em; text-transform:uppercase;
    }}
    .brand {{ font:700 17px/1 var(--serif); letter-spacing:0; text-transform:none; margin-right:auto; }}
    .topbar a {{ text-decoration:none; color:var(--muted); }}
    .topbar a:hover {{ color:var(--ink); }}
    .wrap {{ width:min(1180px, calc(100% - 44px)); margin:0 auto; }}
    .hero {{ padding:62px 0 38px; display:grid; grid-template-columns:minmax(0,1.65fr) minmax(300px,.75fr); gap:48px; align-items:end; }}
    .kicker {{ margin:0 0 18px; font:700 11px/1 var(--sans); letter-spacing:.2em; text-transform:uppercase; }}
    .kicker span {{ color:var(--gold); }}
    h1 {{ margin:0; max-width:14ch; font-size:clamp(52px,7vw,94px); line-height:.92; letter-spacing:-.045em; font-weight:600; }}
    .standfirst {{ margin:26px 0 0; max-width:66ch; font-size:20px; line-height:1.5; font-style:italic; }}
    .verdict {{
      padding:25px 26px; background:var(--ink); color:var(--sheet); border-top:7px solid var(--gold);
      box-shadow:11px 11px 0 var(--gold-soft);
    }}
    .verdict .label {{ font:700 10px/1 var(--sans); letter-spacing:.17em; text-transform:uppercase; color:#d9c991; }}
    .verdict h2 {{ margin:12px 0 10px; font-size:31px; line-height:1.05; }}
    .verdict p {{ margin:0; color:#ded9ce; font:14px/1.55 var(--sans); }}
    .evidence-strip {{
      display:grid; grid-template-columns:repeat(5,1fr); border-top:1px solid var(--ink); border-bottom:1px solid var(--ink);
      margin:24px 0 78px;
    }}
    .metric {{ padding:20px 18px; border-right:1px solid var(--line); }}
    .metric:last-child {{ border-right:0; }}
    .metric strong {{ display:block; font:600 31px/1 var(--serif); }}
    .metric span {{ display:block; margin-top:8px; color:var(--muted); font:700 9px/1.25 var(--sans); letter-spacing:.13em; text-transform:uppercase; }}
    section {{ margin:0 0 86px; scroll-margin-top:74px; }}
    .section-head {{ display:grid; grid-template-columns:140px 1fr; gap:24px; border-top:5px solid var(--ink); padding-top:14px; margin-bottom:28px; }}
    .section-no {{ color:var(--gold); font:700 11px/1.3 var(--sans); letter-spacing:.18em; text-transform:uppercase; }}
    .section-head h2 {{ margin:0; font-size:42px; line-height:1; letter-spacing:-.025em; }}
    .section-head p {{ grid-column:2; margin:0; color:var(--muted); max-width:72ch; font-size:17px; }}
    .grid-2 {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:22px; }}
    .grid-3 {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:18px; }}
    .card {{ background:var(--sheet); border:1px solid var(--line); border-top:4px solid var(--ink); padding:24px; }}
    .card h3 {{ margin:0 0 10px; font-size:24px; line-height:1.12; }}
    .card p {{ margin:0; color:var(--muted); }}
    .card .eyebrow {{ color:var(--gold); font:700 9px/1 var(--sans); letter-spacing:.15em; text-transform:uppercase; margin-bottom:11px; }}
    .recommended {{ border-top-color:var(--green); background:linear-gradient(145deg,var(--sheet),var(--green-soft)); }}
    .rejected {{ border-top-color:var(--red); }}
    .architecture {{ padding:30px; background:var(--sheet); border:1px solid var(--line); }}
    .flow {{ display:grid; grid-template-columns:1fr 44px 1fr 44px 1.2fr; align-items:stretch; gap:8px; }}
    .flow-box {{ border:1px solid var(--ink); padding:20px; min-height:142px; background:var(--paper); }}
    .flow-box strong {{ display:block; font:700 11px/1.2 var(--sans); letter-spacing:.12em; text-transform:uppercase; margin-bottom:12px; }}
    .flow-box p {{ margin:0; color:var(--muted); font-size:14px; }}
    .flow-split {{ display:grid; gap:8px; }}
    .flow-split .flow-box {{ min-height:0; padding:15px; }}
    .arrow {{ display:grid; place-items:center; font:30px/1 var(--serif); color:var(--gold); }}
    .callout {{ margin-top:18px; padding:16px 18px; border-left:5px solid var(--gold); background:var(--gold-soft); font:14px/1.5 var(--sans); }}
    .chart {{ background:var(--sheet); border:1px solid var(--line); padding:24px; }}
    .chart h3 {{ margin:0 0 6px; font-size:24px; }}
    .chart > p {{ margin:0 0 22px; color:var(--muted); font-size:14px; }}
    .chart-group {{ padding:14px 0; border-top:1px solid var(--line); }}
    .chart-group > p {{ margin:0 0 10px; font:700 11px/1 var(--sans); letter-spacing:.08em; text-transform:uppercase; }}
    .bar-row {{ display:grid; grid-template-columns:124px 1fr 82px; gap:12px; align-items:center; margin:9px 0; }}
    .bar-label,.bar-value {{ font:11px/1.2 var(--sans); color:var(--muted); }}
    .bar-value {{ text-align:right; color:var(--ink); font-family:var(--mono); }}
    .bar-track {{ height:10px; background:#e4ded0; overflow:hidden; }}
    .bar-fill {{ display:block; height:100%; min-width:2px; }}
    .bar-fill.markdown {{ background:var(--gold); }}
    .bar-fill.kuzu {{ background:var(--blue); }}
    .bar-fill.files {{ background:var(--red); }}
    .bar-fill.projection {{ background:var(--green); }}
    .table-wrap {{ overflow:auto; border:1px solid var(--line); background:var(--sheet); }}
    table {{ width:100%; border-collapse:collapse; font:12px/1.4 var(--sans); }}
    th {{ position:sticky; top:43px; z-index:2; text-align:left; padding:11px 12px; background:var(--ink); color:var(--sheet); font-size:9px; letter-spacing:.13em; text-transform:uppercase; }}
    td {{ padding:12px; border-bottom:1px solid var(--line); vertical-align:top; }}
    tbody tr:hover {{ background:#f1ead8; }}
    .hash {{ display:block; color:var(--muted); font:9px/1.4 var(--mono); }}
    .badge {{ display:inline-block; padding:3px 7px; border:1px solid currentColor; font:700 8px/1 var(--sans); letter-spacing:.12em; text-transform:uppercase; }}
    .badge.pass {{ color:var(--green); }} .badge.fail {{ color:var(--red); }}
    .case-id {{ display:block; color:var(--muted); font:9px/1.4 var(--mono); }}
    .latency {{ color:var(--muted); font:10px/1.5 var(--mono); }}
    code,.mono {{ font-family:var(--mono); font-size:.9em; }}
    td code {{ white-space:normal; color:#433f36; }}
    .filters {{ display:flex; flex-wrap:wrap; gap:8px; margin:0 0 14px; }}
    .filter {{ border:1px solid var(--ink); background:transparent; color:var(--ink); padding:7px 11px; cursor:pointer; font:700 9px/1 var(--sans); letter-spacing:.1em; text-transform:uppercase; }}
    .filter.active,.filter:hover {{ background:var(--ink); color:var(--sheet); }}
    .authority-card {{ display:grid; grid-template-columns:1.1fr 1fr; background:var(--ink); color:var(--sheet); }}
    .authority-copy {{ padding:34px; }}
    .authority-copy h3 {{ margin:0 0 12px; font-size:35px; line-height:1.05; }}
    .authority-copy p {{ color:#d4cfc5; }}
    .authority-proof {{ padding:28px; background:#232019; }}
    .proof-row {{ display:flex; justify-content:space-between; gap:20px; padding:11px 0; border-bottom:1px solid #4b463c; font:12px/1.3 var(--sans); }}
    .proof-row span {{ color:#bdb5a6; }} .proof-row strong {{ color:#e7d38f; text-align:right; }}
    .graph-panel {{ background:#171510; color:#fff; padding:20px; border-top:6px solid var(--gold); }}
    .graph-panel svg {{ width:100%; height:auto; display:block; }}
    .graph-legend {{ display:flex; gap:18px; flex-wrap:wrap; margin-top:10px; color:#c8c2b7; font:10px/1 var(--sans); }}
    .dot {{ display:inline-block; width:9px; height:9px; margin-right:5px; border-radius:50%; }}
    .finding {{ position:relative; padding-left:40px; }}
    .finding .n {{ position:absolute; left:0; top:0; color:var(--gold); font:700 21px/1 var(--mono); }}
    .finding h3 {{ margin:0 0 7px; font-size:21px; }}
    .finding p {{ margin:0; color:var(--muted); font-size:14px; }}
    .decision-table td:first-child {{ width:23%; font-weight:700; }}
    .yes {{ color:var(--green); font-weight:700; }} .no {{ color:var(--red); font-weight:700; }} .mixed {{ color:#855e16; font-weight:700; }}
    .recommendation {{ background:var(--green); color:white; padding:40px; display:grid; grid-template-columns:1fr 1fr; gap:38px; }}
    .recommendation h3 {{ margin:0; font-size:43px; line-height:1; }}
    .recommendation p,.recommendation li {{ color:#e5eee2; }}
    .recommendation ol {{ margin:0; padding-left:22px; }}
    .recommendation li {{ margin:0 0 11px; }}
    .limitations {{ columns:2; column-gap:42px; color:var(--muted); }}
    .limitations li {{ break-inside:avoid; margin-bottom:9px; }}
    .source-list {{ display:grid; grid-template-columns:repeat(2,1fr); gap:10px 26px; font:13px/1.45 var(--sans); }}
    .source-list p {{ margin:0; padding:10px 0; border-top:1px solid var(--line); }}
    footer {{ border-top:1px solid var(--ink); padding:24px 0 50px; color:var(--muted); display:flex; justify-content:space-between; gap:30px; font:10px/1.5 var(--sans); letter-spacing:.05em; }}
    .hidden {{ display:none; }}
    @media (max-width:900px) {{
      .hero,.authority-card,.recommendation {{ grid-template-columns:1fr; }}
      .evidence-strip {{ grid-template-columns:repeat(2,1fr); }}
      .grid-2,.grid-3 {{ grid-template-columns:1fr; }}
      .flow {{ grid-template-columns:1fr; }} .arrow {{ transform:rotate(90deg); height:30px; }}
      .section-head {{ grid-template-columns:1fr; }} .section-head p {{ grid-column:1; }}
      .topbar a:not(.brand) {{ display:none; }}
    }}
    @media (max-width:600px) {{
      .wrap {{ width:min(100% - 26px,1180px); }} h1 {{ font-size:54px; }}
      .evidence-strip {{ grid-template-columns:1fr 1fr; margin-bottom:58px; }}
      .metric {{ padding:14px 10px; }} .metric strong {{ font-size:24px; }}
      .bar-row {{ grid-template-columns:94px 1fr 64px; gap:7px; }}
      .limitations,.source-list {{ columns:1; display:block; }}
    }}
    @media print {{
      .topbar,.filters {{ display:none; }} body {{ background:white; }}
      section {{ break-inside:avoid; }} .wrap {{ width:100%; }}
    }}
  </style>
</head>
<body>
  <nav class="topbar">
    <a class="brand" href="#top">SoT Systems Lab</a>
    <a href="#method">Method</a>
    <a href="#accuracy">Accuracy</a>
    <a href="#results">Results</a>
    <a href="#cases">Cases</a>
    <a href="#decision">Decision</a>
  </nav>

  <main id="top" class="wrap">
    <header class="hero">
      <div>
        <p class="kicker">PRD-CE Architecture Experiment <span>№ 01</span> · {escape(generated)}</p>
        <h1>{escape(hero_title)}</h1>
        <p class="standfirst">{escape(hero_summary)}</p>
      </div>
      <aside class="verdict">
        <span class="label">Measured decision</span>
        <h2>{escape(verdict_title)}</h2>
        <p>{escape(verdict_summary)}</p>
      </aside>
    </header>

    <div class="evidence-strip" aria-label="Experiment summary">
      <div class="metric"><strong>{'100%' if all_exact else fmt_number(min(markdown['exact_rate'], graph['exact_rate']) * 100, 0) + '%'}</strong><span>literal source fidelity</span></div>
      <div class="metric"><strong>{semantic_exact}/{semantic_assessed}</strong><span>semantic verdicts matched</span></div>
      <div class="metric"><strong>{len(lifecycle_covered)}/{len(lifecycle_expected)}</strong><span>PRD stages represented</span></div>
      <div class="metric"><strong>{total_nodes:,}</strong><span>defined ID nodes</span></div>
      <div class="metric"><strong>{total_files:,}</strong><span>read-only source files</span></div>
    </div>

    <section id="decision-summary">
      <div class="section-head">
        <span class="section-no">00 · Answer first</span>
        <h2>{escape(decision_heading)}</h2>
        <p>{escape(measured_decision)}</p>
      </div>
      <div class="grid-3">
        <article class="card">
          <p class="eyebrow">{escape('Measured winner · current scope' if accepted else 'Acceptance status')}</p>
          <h3>{escape(current_scope_title)}</h3>
          <p>{escape(current_scope_summary)}</p>
        </article>
        <article class="card rejected">
          <p class="eyebrow">Kuzu as authority</p>
          <h3>Strong traversal, wrong governance boundary</h3>
          <p>Cypher and adjacency storage fit the ID graph. A binary store weakens pull-request review and creates migration, backup, schema, and toolchain obligations. Upstream is archived.</p>
        </article>
        <article class="card recommended">
          <p class="eyebrow">Conditional next experiment</p>
          <h3>Markdown authority + graph projection</h3>
          <p>Keep one write path and one conflict rule: files win. Add a graph only if a combined-corpus test proves value for portfolio impact, graph algorithms, or operational graph health.</p>
        </article>
      </div>
    </section>

    <section id="accuracy">
      <div class="section-head">
        <span class="section-no">01 · Accuracy boundaries</span>
        <h2>Four questions stay separate; no blended “accuracy” score.</h2>
        <p>The storage benchmark answers literal source fidelity only. Semantic truth, epistemic conformance, and lifecycle conformance use separate deterministic checks because a graph can reproduce an authored edge perfectly while the edge itself is wrong.</p>
      </div>
      <div class="grid-2">
        <article class="card">
          <p class="eyebrow">1 · Source fidelity</p>
          <h3>{total_cases} checked ID-set cases</h3>
          <p>Both arms share one parser and neutral snapshot. Their parity proves storage and query equivalence for this extraction—not independent raw-Markdown interpretation and not end-to-end answer quality.</p>
        </article>
        <article class="card finding">
          <p class="eyebrow">2 · Semantic truth</p>
          <h3>{semantic_exact} of {semantic_assessed} expected verdicts</h3>
          <p>Pack-style deterministic checks flag title/meaning conflicts and placeholder adoption evidence separately from the literal edges that carried them.</p>
        </article>
        <article class="card">
          <p class="eyebrow">3 · Epistemic conformance</p>
          <h3>Backend-neutral companion suite</h3>
          <p>Immutable revisions test scoped identity, provenance, lifecycle transitions, half-open valid/transaction time, supersession, ambiguous-current fail-closed behavior, and the assertion/evidence boundary.</p>
        </article>
        <article class="card">
          <p class="eyebrow">4 · Lifecycle manifest + gate conformance</p>
          <h3>{len(lifecycle_covered)} of {len(lifecycle_expected)} stages represented</h3>
          <p>The manifest checks stage labels and anchor-family fit; it does not claim a product passed those stages. A separate strict gate oracle blocks incomplete counts, fields, edges, failed attestations, inactive IDs, and silent contract drift.</p>
        </article>
      </div>
      <div class="table-wrap" style="margin-top:22px">
        <table>
          <thead><tr><th>Semantic case</th><th>Lifecycle</th><th>Expected</th><th>Observed</th><th>Detector finding</th></tr></thead>
          <tbody>{render_semantic_rows(semantic_checks)}</tbody>
        </table>
      </div>
    </section>

    <section id="method">
      <div class="section-head">
        <span class="section-no">02 · Method</span>
        <h2>Same corpus. Same parser. Same reviewed manifest answers.</h2>
        <p>Both engines received one neutral graph snapshot. That control matters: otherwise a better parser could masquerade as a better database. GearHeart repositories were read in place and were not modified; only aliases, fingerprints, aggregate metrics, IDs, and relative evidence paths enter this report.</p>
      </div>
      <div class="architecture">
        <div class="flow">
          <div class="flow-box">
            <strong>Read-only inputs</strong>
            <p>HeartBeat · AgentHunt · HomeFalcon<br><br>README + PRD + SoT + EPIC Markdown at pinned git commits.</p>
          </div>
          <div class="arrow">→</div>
          <div class="flow-box">
            <strong>Neutral GraphSnapshot</strong>
            <p>Corpus-scoped entries, source path + line, body hash, definition status, typed hint, and reference edges.</p>
          </div>
          <div class="arrow">→</div>
          <div class="flow-split">
            <div class="flow-box"><strong>Markdown engine</strong><p>Ephemeral Python adjacency map</p></div>
            <div class="flow-box"><strong>Kuzu engine</strong><p>Local property graph, v0.11.3</p></div>
          </div>
        </div>
        <div class="callout"><strong>Quality order:</strong> correctness first, then query cost, context payload, storage, staleness, recovery, and authoring governance. A faster wrong answer is still wrong.</div>
      </div>
      <div class="table-wrap" style="margin-top:22px">
        <table>
          <thead><tr><th>Corpus</th><th>Files</th><th>Nodes</th><th>Edges</th><th>Dangling</th><th>Parse</th><th>Kuzu build</th><th>Markdown</th><th>Kuzu DB</th></tr></thead>
          <tbody>{render_corpus_table(corpora)}</tbody>
        </table>
      </div>
    </section>

    <section id="results">
      <div class="section-head">
        <span class="section-no">03 · Measured results</span>
        <h2>At this scale, Kuzu adds capability—not free performance.</h2>
        <p>{escape('Both engines returned every manifest-authored literal evidence set exactly. ' if source_fidelity_accepted else 'The source-fidelity acceptance check did not pass. ')}{escape(query_winner)} had the lower median warm-query time ({fmt_ms(markdown['median_query_ms'])} versus {fmt_ms(graph['median_query_ms'])}). This small-corpus microbenchmark is not a scalability claim. Kuzu's potential advantage is declarative, persistent graph traversal; this run measured its build, disk, synchronization, and dependency costs but did not test portfolio queries or graph algorithms.</p>
      </div>
      <div class="grid-2">
        <div class="chart">
          <h3>Warm query latency</h3>
          <p>Median across {total_cases} retrieval cases; lower is better. Both ran after one warm-up.</p>
          {render_query_chart(rollup)}
        </div>
        <div class="chart">
          <h3>Context payload is a retrieval choice</h3>
          <p>Median bytes for whole source files versus precise entries and lean projections. Kuzu payload fields were read back from the database; both systems returned identical content.</p>
          {render_payload_chart(rollup)}
        </div>
        <div class="chart">
          <h3>Cold preparation</h3>
          <p>Markdown parsing is required by both; Kuzu then materializes the snapshot.</p>
          {render_build_chart(corpora)}
        </div>
        <div class="chart">
          <h3>Persistent storage</h3>
          <p>Combined Kuzu storage was {aggregate_storage_ratio:,.1f}× combined source size; individual corpora ranged from {min(storage_ratios):,.1f}× to {max(storage_ratios):,.1f}×.</p>
          {render_storage_chart(corpora)}
        </div>
      </div>
      <div class="callout"><strong>The anti-hype result:</strong> exact-entry parsing delivered the same context-density benefit as Kuzu. A graph database would need to earn its added cost in a follow-up test of combined-corpus traversal, graph algorithms, or incremental impact analysis—not smaller prompts alone.</div>
    </section>

    <section id="authority">
      <div class="section-head">
        <span class="section-no">04 · Authority test</span>
        <h2>The harness found a stale projection after one file edit.</h2>
        <p>The harness copied one corpus into an isolated temporary directory, changed one entry, and manually compared its hash with the untouched graph. No product source was edited. The old graph retained its old content hash until a complete rebuild restored parity; no automatic runtime guard was implemented.</p>
      </div>
      <div class="authority-card">
        <div class="authority-copy">
          <h3>Staleness is not theoretical.</h3>
          <p>Any derived index needs invalidation after source changes; a persistent graph also needs reconciliation across processes and commits. Source hashes, stale status, and fail-closed gates are requirements from the experiment, not features completed by this prototype.</p>
        </div>
        <div class="authority-proof">
          <div class="proof-row"><span>Test corpus</span><strong>{escape(DISPLAY_NAMES.get(authority.get('corpus',''), authority.get('corpus','—')))}</strong></div>
          <div class="proof-row"><span>Source changed</span><strong>1 Markdown file</strong></div>
          <div class="proof-row"><span>Harness hash comparison</span><strong>{'STALE' if authority.get('cached_graph_was_stale') else 'not stale'}</strong></div>
          <div class="proof-row"><span>Automatic runtime guard</span><strong>NOT IMPLEMENTED</strong></div>
          <div class="proof-row"><span>Old graph matched new source</span><strong>{'yes' if authority.get('cached_hash_matched_new_source') else 'NO'}</strong></div>
          <div class="proof-row"><span>Rebuild restored parity</span><strong>{'YES' if authority.get('rebuilt_hash_matched_new_source') else 'no'}</strong></div>
          <div class="proof-row"><span>Recovery cost</span><strong>{fmt_ms(authority.get('rebuild_ms',0))}</strong></div>
          <div class="proof-row"><span>Human-reviewable DB diff</span><strong>NO · binary</strong></div>
        </div>
      </div>
    </section>

    <section id="graph">
      <div class="section-head">
        <span class="section-no">05 · What the graph reveals</span>
        <h2>Connectivity is useful; connectivity is not correctness.</h2>
        <p>The sample below captures three observed patterns: repeated raw IDs kept apart by per-corpus isolation, a clean directed Source-of-Truth projection, and an authored directed link whose meaning is wrong. Kuzu faithfully returns the authored edges; it does not validate their semantics.</p>
      </div>
      <div class="graph-panel">
        <svg viewBox="0 0 1100 460" role="img" aria-label="Observed PRD-CE identifiers and directed relationships">
          <defs>
            <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#8d877d"/></marker>
            <filter id="glow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
          </defs>
          <g stroke="#706b62" stroke-width="1.5" fill="none" marker-end="url(#arrowhead)">
            <path d="M488 135 C565 128 595 100 660 92"/>
            <path d="M488 135 C565 142 595 170 660 178"/>
            <path d="M482 350 C560 342 595 322 660 316"/>
            <path d="M482 350 C560 360 595 391 660 398"/>
          </g>
          <g font-family="SFMono-Regular,Consolas,monospace" font-size="13" text-anchor="middle">
            <text x="122" y="34" fill="#d9c991" font-size="11">SAME RAW ID · THREE PRODUCTS</text>
            <g><circle cx="120" cy="105" r="34" fill="#a77f23"/><text x="120" y="110" fill="#fff">HB</text><rect x="47" y="135" width="146" height="28" rx="14" fill="#2a2721"/><text x="120" y="154" fill="#fff">BR-001 · BYOK</text></g>
            <g><circle cx="120" cy="235" r="34" fill="#315b70"/><text x="120" y="240" fill="#fff">AH</text><rect x="38" y="265" width="164" height="28" rx="14" fill="#2a2721"/><text x="120" y="284" fill="#fff">BR-001 · Discovery</text></g>
            <g><circle cx="120" cy="365" r="34" fill="#62506d"/><text x="120" y="370" fill="#fff">HF</text><rect x="33" y="395" width="174" height="28" rx="14" fill="#2a2721"/><text x="120" y="414" fill="#fff">BR-001 · Free tier</text></g>

            <text x="560" y="34" fill="#d9c991" font-size="11">OBSERVED HEARTBEAT OUTBOUND LINKS</text>
            <g filter="url(#glow)"><circle cx="440" cy="135" r="44" fill="#38623a"/><text x="440" y="140" fill="#fff">ARC-001</text></g>
            <g><circle cx="700" cy="90" r="38" fill="#315b70"/><text x="700" y="95" fill="#fff">DBT-003</text></g>
            <g><circle cx="700" cy="180" r="38" fill="#315b70"/><text x="700" y="185" fill="#fff">DBT-004</text></g>

            <text x="563" y="263" fill="#d9c991" font-size="11">OBSERVED HOMEFALCON OUTBOUND LINKS</text>
            <g><circle cx="440" cy="350" r="42" fill="#62506d"/><text x="440" y="355" fill="#fff">TECH-007</text></g>
            <g><circle cx="700" cy="315" r="40" fill="#9a3c2f"/><text x="700" y="320" fill="#fff">UJ-007</text></g>
            <g><circle cx="700" cy="400" r="40" fill="#9a3c2f"/><text x="700" y="405" fill="#fff">UJ-008</text></g>
            <text x="780" y="302" fill="#e7b9af" text-anchor="start" font-family="Helvetica Neue,Arial,sans-serif">Authored labels imply Command Center / Impact Report</text>
            <text x="780" y="326" fill="#b9b3a8" text-anchor="start" font-family="Helvetica Neue,Arial,sans-serif">Canonical UJ-007 = Product Inventory</text>
            <text x="780" y="411" fill="#b9b3a8" text-anchor="start" font-family="Helvetica Neue,Arial,sans-serif">Canonical UJ-008 = Product Detail</text>
          </g>
        </svg>
        <div class="graph-legend">
          <span><i class="dot" style="background:#a77f23"></i>business rule</span>
          <span><i class="dot" style="background:#38623a"></i>architecture decision</span>
          <span><i class="dot" style="background:#315b70"></i>data/cache</span>
          <span><i class="dot" style="background:#9a3c2f"></i>semantic conflict requiring human review</span>
        </div>
      </div>
    </section>

    <section id="cases">
      <div class="section-head">
        <span class="section-no">06 · Source-fidelity suite</span>
        <h2>Every literal retrieval case, side by side.</h2>
        <p>“Exact” means the returned ID set equals the manifest-authored, separately reviewed Markdown evidence set. Latency is a warm median across {data['runtime']['repeats_per_case']} repetitions. It does not mean the authored knowledge is semantically correct; those verdicts appear in the separate accuracy panel.</p>
      </div>
      <div class="filters" aria-label="Filter benchmark cases">
        <button class="filter active" data-filter="all">All</button>
        <button class="filter" data-filter="heartbeat">HeartBeat</button>
        <button class="filter" data-filter="agenthunt">AgentHunt</button>
        <button class="filter" data-filter="homefalcon">HomeFalcon</button>
        <button class="filter" data-filter="traverse">Traversal</button>
        <button class="filter" data-filter="lookup">Lookup</button>
      </div>
      <div class="table-wrap">
        <table id="case-table">
          <thead><tr><th>Question</th><th>Corpus</th><th>Markdown</th><th>Kuzu</th><th>Retrieved evidence IDs</th></tr></thead>
          <tbody>{render_case_rows(data['cases'])}</tbody>
        </table>
      </div>
    </section>

    <section id="findings">
      <div class="section-head">
        <span class="section-no">07 · Quality-control findings</span>
        <h2>The prototype found design risks beyond speed.</h2>
        <p>Each surfaced while projecting three live PRD-CE products through the same repeatable model. The run kept one database per corpus; a combined portfolio graph remains untested.</p>
      </div>
      <div class="grid-2">
        <article class="card finding"><span class="n">1</span><h3>IDs require a project namespace</h3><p><code>BR-001</code> has different meanings in all three corpora. This run avoided collision through separate databases. A future combined graph must test a composite identity such as <code>(project_id, id_ref)</code>.</p></article>
        <article class="card finding"><span class="n">2</span><h3>Edges can be precisely wrong</h3><p>HomeFalcon <code>TECH-007</code> links <code>UJ-007/008</code> as Command Center / Impact Report, while the canonical journey definitions are Product Inventory / Product Detail. Traversal cannot replace semantic validation.</p></article>
        <article class="card finding"><span class="n">3</span><h3>Markdown grammar is part of the schema</h3><p>Compound IDs, PRD/README table-owned IDs, nested headings, revision sections, and duplicate definitions all occur in real products. A heading-only regex silently drops knowledge.</p></article>
        <article class="card finding"><span class="n">4</span><h3>Provenance must survive materialization</h3><p>Each node and edge needs repo, relative path, line/anchor, content hash, commit, extraction confidence, and last-indexed time. Without them a graph answer cannot be audited back to authority.</p></article>
        <article class="card finding"><span class="n">5</span><h3>Graph health is not product truth health</h3><p>A structurally valid edge may still be stale or semantically inconsistent. Graph checks should flag orphans, dangling refs, staleness, duplicate definitions, and cross-authority contradictions separately.</p></article>
        <article class="card finding"><span class="n">6</span><h3>Kuzu lifecycle risk is material</h3><p>The exact upstream requested is archived. The final release remains usable, but production adoption would inherit compatibility and security maintenance with no authoritative roadmap.</p></article>
      </div>
    </section>

    <section id="decision">
      <div class="section-head">
        <span class="section-no">08 · Tradeoff decision</span>
        <h2>{escape('Markdown wins now; the graph must earn a second job.' if accepted else 'Decision withheld until benchmark acceptance passes.')}</h2>
        <p>{escape(measured_decision)}</p>
      </div>
      <div class="table-wrap">
        <table class="decision-table">
          <thead><tr><th>Decision dimension</th><th>Markdown only</th><th>Kuzu as SoT</th><th>Strict hybrid</th></tr></thead>
          <tbody>
            <tr><td>Human authoring & review</td><td class="yes">Best · familiar text + PR diffs</td><td class="no">Weak · requires application/editor</td><td class="yes">Best · Markdown write path</td></tr>
            <tr><td>Git history & branching</td><td class="yes">Native</td><td class="no">Binary/migration burden</td><td class="yes">Native authority; cache rebuilt per commit</td></tr>
            <tr><td>Exact ID lookup</td><td class="yes">Exact in benchmark</td><td class="yes">Exact in benchmark</td><td class="yes">Exact, with source fallback</td></tr>
            <tr><td>Reverse / multi-hop queries</td><td class="yes">Exact + fastest in this run</td><td class="yes">Exact; Python orchestrated one-hop Cypher</td><td class="mixed">Potential, not separately tested</td></tr>
            <tr><td>Context density</td><td class="yes">Exact entry extraction works</td><td class="yes">Projection queries work</td><td class="yes">Choose entry or projection by task</td></tr>
            <tr><td>Staleness risk</td><td class="yes">One copy</td><td class="mixed">Low only if sole authority</td><td class="mixed">Managed by hash/commit + fail-closed</td></tr>
            <tr><td>Offline portability</td><td class="yes">Any text tool</td><td class="no">Runtime + schema + binary</td><td class="mixed">Files portable; graph optional</td></tr>
            <tr><td>Operational burden</td><td class="yes">Lowest</td><td class="no">Highest</td><td class="mixed">Moderate and bounded</td></tr>
            <tr><td>Portfolio-scale graph analysis</td><td class="mixed">Not tested</td><td class="mixed">Not tested</td><td class="mixed">Hypothesis for follow-up</td></tr>
            <tr><td>Current dependency outlook</td><td class="yes">Open format</td><td class="no">Kuzu archived</td><td class="mixed">Engine-swappable projection</td></tr>
          </tbody>
        </table>
      </div>
      <div class="recommendation" style="margin-top:24px">
        <h3>{escape('Current decision: keep Markdown. Gate any graph projection.' if accepted else 'No current decision: resolve the failed acceptance checks first.')}</h3>
        <ol>
          <li>Define one engine-neutral <code>GraphSnapshot</code> contract from canonical files.</li>
          <li>Keep the in-memory backend as the correctness and cost baseline.</li>
          <li>Test a combined corpus keyed by <code>(project_id, id_ref)</code>, never raw ID alone.</li>
          <li>Persist source path, line, hash, commit, confidence, and extraction warnings.</li>
          <li>Require incremental rebuild, explicit stale status, and fail-closed gates.</li>
          <li>Adopt a graph only if portfolio impact or algorithms beat the baseline materially.</li>
          <li>Keep every product definition edit in Markdown and git. On conflict, repo wins.</li>
          <li>Do not standardize production on archived Kuzu without a separate successor evaluation.</li>
        </ol>
      </div>
    </section>

    <section id="next">
      <div class="section-head">
        <span class="section-no">09 · If you continue</span>
        <h2>Define the next proof before choosing an engine.</h2>
        <p>{escape('The experiment supports a neutral contract and a stronger follow-up, not immediate graph adoption.' if accepted else 'The persisted evidence supports debugging the failed acceptance checks; it does not support an architecture direction yet.')} Set measurable success criteria before adding another persistent system.</p>
      </div>
      <div class="grid-3">
        <article class="card"><p class="eyebrow">M0 · Extract</p><h3>Canonical GraphSnapshot</h3><p>Harden compound IDs, table definitions, duplicate provenance, range syntax, relation confidence, and source/commit fingerprints. Emit deterministic JSON.</p></article>
        <article class="card"><p class="eyebrow">M1 · Prove</p><h3>Combined-corpus challenge</h3><p>Test composite identity, portfolio impact, graph algorithms, incremental updates, and end-to-end evidence retrieval against the in-memory baseline.</p></article>
        <article class="card"><p class="eyebrow">M2 · Decide</p><h3>Adopt only on measured lift</h3><p>Add a read-only projection only if the combined test shows material value after build, storage, staleness, and lifecycle costs. Markdown remains authoritative either way.</p></article>
      </div>
    </section>

    <section id="limits">
      <div class="section-head">
        <span class="section-no">10 · Limits & provenance</span>
        <h2>What this evidence does not prove.</h2>
        <p>{escape('A useful experiment is explicit about its boundary. These results support an architecture direction, not a universal database benchmark.' if accepted else 'A useful experiment is explicit about its boundary. This run is evidence for resolving failed acceptance checks, not an architecture decision or a universal database benchmark.')}</p>
      </div>
      <ul class="limitations">
        <li>Three local products are a realistic but small sample; PetPass's flat legacy layout was not part of the timed corpus.</li>
        <li>The benchmark measures deterministic evidence retrieval, not end-to-end LLM answer quality.</li>
        <li>Warm microseconds on hundreds of nodes do not predict million-node graph performance.</li>
        <li>Both engines share one parser by design; parser defects affect both equally and are reported separately.</li>
        <li>The Kuzu build uses parameterized inserts for clarity, not a tuned bulk-import pipeline.</li>
        <li>The run used one database per corpus; it did not implement or test a combined <code>(project_id, id_ref)</code> namespace.</li>
        <li>Two-hop Kuzu traversal was orchestrated as repeated one-hop Cypher calls in Python; variable-length Cypher and graph algorithms were not benchmarked.</li>
        <li>Incremental indexing, concurrent edits, operational recovery, and end-to-end LLM outcomes were not tested.</li>
        <li>Latest-visible evidence precedence and explicit verification resolution are tested, but freshness-policy TTL expiry and scheduled re-review are not implemented or tested.</li>
        <li>Payload size estimates compare whole-file, exact-entry, and structured projections; actual agent tokenization varies.</li>
        <li>Committed evidence includes aliases, IDs, questions, relative evidence locations, selected semantic titles, commits, and fingerprints; source bodies, absolute paths, and PII are excluded.</li>
        <li>Two deterministic semantic checks expose known defects; broad ontology validation, blind agent evaluation, and human adjudication remain future work.</li>
      </ul>
      <div class="source-list" style="margin-top:28px">
        <p><strong>Kuzu upstream</strong><br><a href="https://github.com/kuzudb/kuzu">github.com/kuzudb/kuzu</a> · archived 2025-10-10</p>
        <p><strong>Final release</strong><br><a href="https://github.com/kuzudb/kuzu/releases/tag/v0.11.3">v0.11.3</a> · commit <code>{escape(data['upstream']['commit'][:12])}</code></p>
        <p><strong>Official docs archive</strong><br><a href="https://kuzudb.github.io/docs/">kuzudb.github.io/docs</a></p>
        <p><strong>Local methodology evidence</strong><br>HeartBeat ARC-001 / DBT-004 / DBT-005 · benchmark case manifest</p>
      </div>
    </section>
  </main>

  <footer class="wrap">
    <span>PRD-CE SoT Systems Lab · generated from bounded benchmark evidence · {escape(generated)}</span>
    <span>Kuzu {escape(data['upstream']['python_package'])} · Python {escape(data['runtime']['python'])} · {escape(data['runtime']['machine'])}</span>
  </footer>

  <script id="benchmark-data" type="application/json">{embedded_data}</script>
  <script>
    const buttons = [...document.querySelectorAll('.filter')];
    const rows = [...document.querySelectorAll('#case-table tbody tr')];
    buttons.forEach(button => button.addEventListener('click', () => {{
      buttons.forEach(item => item.classList.remove('active'));
      button.classList.add('active');
      const filter = button.dataset.filter;
      rows.forEach(row => {{
        const visible = filter === 'all' || row.dataset.corpus === filter || row.dataset.kind === filter || row.dataset.status === filter;
        row.classList.toggle('hidden', !visible);
      }});
    }}));
  </script>
</body>
</html>
"""

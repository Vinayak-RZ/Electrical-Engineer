import { register } from "./registry.js";
import { renderSlot } from "./registry.js";
import { useLayout } from "../store.js";
import { useEffect, useState } from "react";

function Root() {
  return (
    <div>
      <a className="skip" href="#workspace">
        Skip to workspace
      </a>
      <header>
        <strong>Electrical Engineer</strong>
      </header>
      <div style={{ display: "flex" }}>
        {renderSlot("sidebar")}
        <main id="workspace">{renderSlot("workspace")}</main>
      </div>
    </div>
  );
}

function Sidebar() {
  const [runs, setRuns] = useState([]);
  const setRun = useLayout((s) => s.setRun);
  useEffect(() => {
    fetch("/api/runs")
      .then((r) => r.json())
      .then((d) => setRuns(d.runs || []))
      .catch(() => setRuns([]));
  }, []);
  return (
    <nav className="card" aria-label="Runs">
      {runs.map((id) => (
        <button key={id} className="asset-row" onClick={() => setRun(id)}>
          {id}
        </button>
      ))}
    </nav>
  );
}

function Workspace() {
  const id = useLayout((s) => s.currentRunId);
  if (!id) return <p>empty</p>;
  return (
    <div>
      {renderSlot("run.detail", { id })}
      {renderSlot("run.artifacts", { id })}
      {renderSlot("photo.confirm", { id })}
    </div>
  );
}

function RunDetail({ id }) {
  const [summary, setSummary] = useState("");
  useEffect(() => {
    fetch(`/api/runs/${id}`)
      .then((r) => r.json())
      .then((d) => setSummary(d.summary || JSON.stringify(d)))
      .catch(() => setSummary(""));
  }, [id]);
  const unchecked = String(summary).includes("unchecked");
  return (
    <section className="card" aria-live="polite">
      <h1>{id}</h1>
      {unchecked ? <span className="badge-pill">unchecked</span> : null}
      <pre className="number-display">{summary}</pre>
    </section>
  );
}

function Artifacts({ id }) {
  return (
    <section className="card">
      <h2>Artifacts</h2>
      <img alt="" src={`/api/runs/${id}/artifact.svg`} width="0" height="0" />
    </section>
  );
}

function PhotoConfirm({ id }) {
  return (
    <section className="card">
      <h2>Confirm topology</h2>
      <button
        className="button-primary"
        type="button"
        onClick={() => fetch(`/api/runs/${id}/confirm`, { method: "POST" })}
      >
        Confirm
      </button>
    </section>
  );
}

register("root", Root);
register("sidebar", Sidebar);
register("workspace", Workspace);
register("run.detail", RunDetail);
register("run.artifacts", Artifacts);
register("photo.confirm", PhotoConfirm);

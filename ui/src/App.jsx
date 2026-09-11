import { renderSlot } from "./slots/registry.js";
import "./slots/root.jsx";

export default function App() {
  return renderSlot("root");
}

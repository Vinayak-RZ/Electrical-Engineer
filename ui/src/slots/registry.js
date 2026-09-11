import { createElement } from "react";

const slots = {};

export function register(name, Component) {
  slots[name] = Component;
}

export function renderSlot(name, props) {
  const Cmp = slots[name];
  if (!Cmp) return null;
  return createElement(Cmp, props);
}

export function registered() {
  return Object.keys(slots).sort();
}

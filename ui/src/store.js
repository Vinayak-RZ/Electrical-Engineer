import { create } from "zustand";

export const useLayout = create((set) => ({
  currentRunId: null,
  setRun: (id) => set({ currentRunId: id }),
}));

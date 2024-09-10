import { configureStore } from "@reduxjs/toolkit";
import { setupListeners } from "@reduxjs/toolkit/query";
import { dbApi } from "./db";

export const store = configureStore({
  reducer: {
    [dbApi.reducerPath]: dbApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(dbApi.middleware),
});

setupListeners(store.dispatch);

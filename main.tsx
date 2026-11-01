
import React from "react";
import * as ReactDOM from "react-dom/client";

import App from "./App";
import "./index.css";

const container = document.getElementById("root");

if (container !== null) {
  const application = ReactDOM.createRoot(container);
  application.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
}

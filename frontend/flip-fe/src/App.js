// src/App.js

import React from "react";
import ColorChanger from "./ColorChanger";
import NewUserForm from "./login";

function App() {
  return (
    <div className="App">
      <NewUserForm />
      <ColorChanger />
    </div>
  );
}

export default App;

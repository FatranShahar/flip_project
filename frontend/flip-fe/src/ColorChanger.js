import React, { useState } from "react";
import axios from "axios";

const ColorChanger = () => {
  const [color, setColor] = useState("green");

  const toggleColor = () => {
    console.log("hey")
    setColor(color === "green" ? "red" : "green");
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        minHeight: "100vh",
      }}
    >
      <div
        style={{
          width: "100px",
          height: "100px",
          backgroundColor: color,
          marginBottom: "10px",
        }}
      />
      <button style={{ margin: "5px auto" }} onClick={toggleColor}>
        Change Color
      </button>
    </div>
  );
};

export default ColorChanger;

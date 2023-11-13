import React, { useState } from "react";
import axios from "axios";

const ColorChanger = () => {
  const [color, setColor] = useState("green");

  const toggleColor = () => {
    axios
      .get("http://localhost:5000/update-color")
      .then((response) => {
        if (response.data.status === 1) {
          setColor("red");
        } else {
          setColor("green");
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
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

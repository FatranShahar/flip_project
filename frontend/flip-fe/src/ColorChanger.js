import React, { useState, useEffect } from "react";
import axios from "axios";

const getFlipCount = async () => {
  try {
    const response = await axios.get("http://localhost:5000/get-current-data");
    return response.data.flips_count;
  } catch (error) {
    console.error("Error fetching flip count:", error);
    throw error;
  }
};

const getColor = async () => {
  console.log("in get color");
  try {
    const response = await axios.get("http://localhost:5000/get-current-data");
    return response.data.status === 1 ? "red" : "green";
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};

const pressedButton = async () => {
  try {
    const response = await axios.get("http://localhost:5000/update-data");
    return response.data.status === 1 ? "red" : "green";
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }

}

const ColorChanger = () => {
  const [color, setColor] = useState("");
  const [flipCount, setFlipCount] = useState(0);

  const toggleColor = async () => {
    try {
      const newColor = await pressedButton();
      setColor(newColor);
      setFlipCount(await getFlipCount()); // Update flip count after button press
    } catch (error) {
      console.error("Error toggling color:", error);
    }
  };

  useEffect(() => {
    getColor().then(initialColor => {
      setColor(initialColor);
    });

    getFlipCount().then(initialFlipCount => {
      setFlipCount(initialFlipCount);
    });
  }, []);

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
      <p>Button Presses: {flipCount}</p>
    </div>
  );
};



export default ColorChanger;

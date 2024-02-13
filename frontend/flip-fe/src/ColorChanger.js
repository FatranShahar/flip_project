import React, { useState, useEffect } from "react";
import axios from "axios";

const ColorChanger = () => {
  const [color, setColor] = useState("");
  const [flipCount, setFlipCount] = useState(0);

  useEffect(() => {
    const fetchData = async () =>{
      try{
        const response = await axios.get("http://localhost:5000/get-current-data"); 
        const newColor = extractColor(response.data.current_state);
        setColor(newColor);
        setFlipCount(getFlipCount(response.data));
        return response;
      } catch (error){
        console.error("Error fetching data:", error);
        throw error; 
      }
    }
    fetchData();
  }, []);

  const getFlipCount = (data) => {
    return data.flips_count;
  };

  const extractColor = (state) => {
    return state == 1 ? "red" : "green";
  };

  const toggleColor = async () => {
    try {
      const response = await axios.get("http://localhost:5000/update-data");
      const newColor = extractColor(response.data.current_state);
      setColor(newColor);
      setFlipCount(getFlipCount(response.data)); // Update flip count after button press
    } catch (error) {
      console.error("Error toggling color:", error);
    }
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
      <p>Button Presses: {flipCount} times</p>
    </div>
  );
};

export default ColorChanger;

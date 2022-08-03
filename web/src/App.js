import "./App.css";

import axios from "axios";
import { useEffect, useState } from "react";

axios.defaults.baseURL = "http://localhost:5000";

const getNotes = () => axios.get("/items").then((res) => res.data);

function App() {
  const [items, setItems] = useState([]);
  useEffect(() => {
    getNotes()
      .then((e) => {
        setItems(Object.keys(e));
      })
      .catch((exception) => console.log("exception:" + exception));
  }, []);
  return <div>{items}</div>;
}

export default App;

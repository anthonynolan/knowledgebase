import "./App.css";

import axios from "axios";
import { useEffect, useState } from "react";

axios.defaults.baseURL = "http://localhost:5000";

const getItems = () => axios.get("/items").then((res) => res.data);

function App() {
  const [items, setItems] = useState([]);
  useEffect(() => {
    getItems()
      .then((e) => setItems(e))
      .catch((exception) => console.log("exception:" + exception));
  }, []);

  return (
    <ul>
      {items.map((item) => (
        <li key={item.name}>{item.name}</li>
      ))}
    </ul>
  );
}

export default App;

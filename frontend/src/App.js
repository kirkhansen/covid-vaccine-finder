import './App.css';
import { useState, useEffect } from "react";
import JsonTable from "ts-react-json-table";

function App() {
  const [data,setData] = useState(null);
  const getData = () => {
    fetch('data.json'
    ,{
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
    }
    )
      .then(function(response){
        return response.json();
      })
      .then(function(myJson) {
        setData(myJson)
      });
  }
  useEffect(()=>{
    getData()
  }, [])

  return (
    <div className="App">
      <JsonTable rows={ data } />
    </div>
  );
}

export default App;

import './App.css';
import moment from 'moment'
import React from "react";
import JsonTable from "ts-react-json-table";


class VaccineTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {data: []};
  }

  getData = () => {
    fetch('data.json'
    ,{
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
    }
    ).then((response) => {
        return response.json();
    }).then((vaccineAvailability) => {
        this.setState({data: vaccineAvailability});
    });
  };

  componentDidMount() {
      this.getData();
  }

  render() {
    return (
      <JsonTable rows={ this.state.data } />
    );
  }
}


class LastUpdated extends React.Component {
  constructor(props) {
    super(props);
    this.state = {lastUpdated: null};
  }

  getLastUpdated = () => {
    fetch('last-updated.json'
    ,{
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
    }
    ).then((response) => {
        return response.json();
    }).then((lastUpdated) => {
        this.setState({
            lastUpdated: moment.unix(lastUpdated["last_updated"]).format("YYYY-MM-DDTHH:mm:ss")
        });
    });
  };

  componentDidMount() {
      this.getLastUpdated();
  }

  render() {
    return (
        <div>
        <h2>Last updated at {this.state.lastUpdated} </h2>
        </div>
    );
  }
}


function App() {

  return (
    <div className="App">
     <LastUpdated />
     <VaccineTable />
    </div>
  );
}

export default App;

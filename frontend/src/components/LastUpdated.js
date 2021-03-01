import moment from "moment";
import React from "react";

export class LastUpdated extends React.Component {
  constructor(props) {
    super(props);
    this.state = { lastUpdated: null };
  }

  getLastUpdated = () => {
    fetch("last-updated.json", {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then((response) => {
        return response.json();
      })
      .then((lastUpdated) => {
        this.setState({
          lastUpdated: moment.unix(lastUpdated["last_updated"]).format("YYYY-MM-DDTHH:mm:ss"),
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

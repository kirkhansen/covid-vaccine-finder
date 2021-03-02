import React from "react";
import { DataGrid } from "@material-ui/data-grid";
import Link from "@material-ui/core/Link";
import CheckCircleIcon from "@material-ui/icons/CheckCircle";
import WarningIcon from "@material-ui/icons/Warning";
import { enumerate } from "./util";
import { green } from "@material-ui/core/colors";

const DATA_COLUMNS = [
  { field: "id", headerName: "id", hide: true },
  {
    field: "available",
    headerName: "Available",
    flex: 0.25,
    renderCell: (params) => (
      <Link href={params.getValue("link")}>
        {params.value === "yes" ? (
          <CheckCircleIcon varient="outlined" style={{ color: green[500] }} />
        ) : (
          <WarningIcon varient="outlined" color="error" />
        )}
      </Link>
    ),
  },
  { field: "provider", headerName: "Provider", flex: 0.25 },
  { field: "store_name", headerName: "Store Name", flex: 0.25 },
  {
    field: "store_address",
    headerName: "Store Address",
    flex: 0.25,
    valueGetter: (params) => `${params.value}, ${params.getValue("store_city")}`,
  },
  { field: "store_city", headerName: "Store City", flex: 0.25, hide: true },
  {
    field: "vaccine_types",
    headerName: "Vaccine Types",
    flex: 0.25,
    valueGetter: (params) => (params.value !== null) ? `${params.value}` : "N/A",
  },
  { field: "link", headerName: "Link", flex: 1, hide: true },
];
const SORT_MODEL = [
  {
    field: "available",
    sort: "desc",
  },
];

export class VaccineTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = { data: [], tableLoading: true };
  }

  getData = () => {
    fetch("data.json", {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then((response) => {
        return response.json();
      })
      .then((vaccineAvailability) => {
        for (let [i, row] of enumerate(vaccineAvailability)) {
          row["id"] = i;
        }
        // let's split it up into available, and not.
        // our component can return two tables with one hidden by default
        this.setState({ data: vaccineAvailability, tableLoading: false });
      });
  };

  componentDidMount() {
    this.getData();
  }

  render() {
    return (
      <DataGrid
        rows={this.state.data}
        columns={DATA_COLUMNS}
        autoHeight={true}
        loading={this.state.tableLoading}
        sortModel={SORT_MODEL}
      />
    );
  }
}

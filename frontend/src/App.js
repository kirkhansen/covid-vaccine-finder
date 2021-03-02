import "./App.css";
import { VaccineTable } from "./components/VaccineTable";
import { LastUpdated } from "./components/LastUpdated";
import { RssFeed } from "./components/RssFeed";
import Alert from "@material-ui/lab/Alert";
import { createMuiTheme, ThemeProvider } from "@material-ui/core/styles";
import { CssBaseline, useMediaQuery } from "@material-ui/core";
import React from "react";

function App() {
  const prefersDarkMode = useMediaQuery("(prefers-color-scheme: dark)");

  const theme = React.useMemo(
    () =>
      createMuiTheme({
        palette: {
          type: prefersDarkMode ? "dark" : "light",
        },
      }),
    [prefersDarkMode]
  );

  return (
    <ThemeProvider theme={theme}>
      <div className="App">
      <CssBaseline />
      <LastUpdated />
      <Alert severity="info"><RssFeed /> Updates published when available vacccine is detected</Alert>
      <Alert severity="info">Icons are clickable; click to be redirected to provider's website</Alert>
      <VaccineTable />
      </div>
    </ThemeProvider>
  );
}

export default App;

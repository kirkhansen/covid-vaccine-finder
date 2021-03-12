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
        <Alert severity="info">
          <RssFeed /> Updates published via RSS when available vacccine is detected. Data aquasition is scheduled to run
          every half hour.
        </Alert>
        <Alert severity="info">Icons are clickable; click to be redirected to provider's website</Alert>
        <VaccineTable />
      </div>
      <footer>
        <Alert severity="info">
          Find a bug? Contact me by
          <a href="https://github.com/kirkhansen/covid-vaccine-finder/issues/new"> making an issue.</a>
        </Alert>
        <Alert severity="warning">
          These data are collected via web scraping from various sources and may be out of date or inaccurate. It's also
          not officially supported by any of the above providers. Please continue to check with all your providers for
          appointment availability.
        </Alert>
        <a href="https://www.buymeacoffee.com/kirkhansen" target="_blank" rel="noreferrer"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-blue.png" alt="Buy Me A Coffee" style={{height: "45px", width: "168px"}}/></a>
      </footer>
    </ThemeProvider>
  );
}

export default App;

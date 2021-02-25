import logo from './logo.svg';
import { ApolloClient, ApolloLink, ApolloProvider, HttpLink, InMemoryCache, concat} from '@apollo/client';
import { createHttpLink } from "apollo-link-http";
import './App.css';
import { HyveeVaccines } from "./Hyvee";

// const _LINK = new HttpLink({uri: "https://www.hy-vee.com/my-pharmacy/api/graphql"});
//
// const _CORS = new ApolloLink((operation, forward) => {
//   operation.setContext({
//     headers: {
//       "Access-Control-Allow-Origin": "*",
//     }
//   });
//   return forward(operation);
// });
//
const _LINK = createHttpLink({
    uri: "https://www.hy-vee.com/my-pharmacy/api/graphql",
    headers: {
        "Access-Control-Allow-Origin": "*",
    },
    fetchOptions: {
        mode: "no-cors",
    },
});



const HYVEE_APOLLO_CLIENT = new ApolloClient({
  cache: new InMemoryCache(),
  link: _LINK,
});

function App() {
  return (
    <ApolloProvider client={HYVEE_APOLLO_CLIENT}>
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <HyveeVaccines />
    </div>
    </ApolloProvider>
  );
}

export default App;

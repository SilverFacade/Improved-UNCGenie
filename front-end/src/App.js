import logo from './logo.svg';
import './App.css';
import {Routes, Route} from "react-router-dom";
import Home from './Components/Home';
import Nav from './Components/Nav';
import Login from './Components/Login';

function App() {
  return (
      <>
          <Nav/>
          <div className={'wrapper'}>
              <Routes>
                  <Route path = {'/home'} element = {<Home />} />
                  <Route path = {'/login'} element = {<Login />} />
              </Routes>
          </div>
      </>
  );
}

export default App;

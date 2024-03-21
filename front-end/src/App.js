import logo from './logo.svg';
import './App.css';
import {Routes, Route} from "react-router-dom";
import Home from './Components/Home';
import Nav from './Components/Nav';
import Login from './Components/Login';
import Register from './Components/Register';
import NotFound from './Components/NotFound';

function App() {
  return (
      <>
          <Nav/>
          <div className={'wrapper'}>
              <Routes>
                  <Route path = {'/'} element = {<Home />} />
                  <Route path = {'/login'} element = {<Login />} />
                  <Route path = {'/register'} element = {<Register />} />
                  <Route path = {'*'} element = {<NotFound />} />
              </Routes>
          </div>
      </>
  );
}

export default App;

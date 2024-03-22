import logo from './logo.svg';
import './App.css';
import {Routes, Route} from "react-router-dom";
import Home from './Components/Home';
import Nav from './Components/Nav';
import Login from './Components/Login';
import Register from './Components/Register';
import ClassInfo from './Components/ClassInfo';
import About from './Components/About';
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
                  <Route path = {'/classInfo'} element = {<ClassInfo />} />
                  <Route path = {'/about'} element = {<About />} />
                  <Route path = {'*'} element = {<NotFound />} />
              </Routes>
          </div>
      </>
  );
}

export default App;

import logo from './logo.svg';
import './App.css';
import {useEffect} from 'react';
import {Routes, Route} from "react-router-dom";
import Home from './Components/Home';
import Login from './Components/Login';
import Register from './Components/Register';
import ClassInfo from './Components/ClassInfo';
import Personal from './Components/PersonalInfo';
import Progress from './Components/Progress';
import NotFound from './Components/NotFound';

function App() {
  return (
      <>
          <div className={'wrapper'}>
              <Routes>
                  <Route path = {'/'} element = {<Home />} />
                  <Route path = {'/login'} element = {<Login />} />
                  <Route path = {'/register'} element = {<Register />} />
                  <Route path = {'/classInfo'} element = {<ClassInfo />} />
                  <Route path = {'/progress'} element = {<Progress />} />
                  <Route path = {'/personal'} element = {<Personal />} />
                  <Route path = {'*'} element = {<NotFound />} />
              </Routes>
          </div>
      </>
  );
}

export default App;

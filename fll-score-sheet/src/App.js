import React from 'react'; //allows you to use reactive stuff
import logo from './logo.svg'; // image import
import './App.css'; //css import

function Example() {
  // NOTE: CLASSES RENDER AS with className
  return (
    <div className="Example"> 
      <header className="Example-header">
        <img src={logo} className="Example-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        
      </header>
    </div>
  );
}

export default Example;

import React from 'react'
import './FirstComponent.css';
import Button from 'react-bootstrap/Button'

function FirstComponent(props) {
  return (
    <div>
        <h3>{props.title}</h3>
        <p>Howdy yall</p>
        <Button>Click me!</Button>
    </div>
  )
}

export default FirstComponent
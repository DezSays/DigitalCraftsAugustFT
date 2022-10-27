import React from 'react'
import { Link } from 'react-router-dom'

// create two components: forms, news
// add components to react-router index.js
// Add the links to base layout 

const BaseLayout = (props) => {
  return (
    <>
        <ul>
            <li><Link to='/'>Home</Link></li>    
            <li><Link to='/forms'>Forms</Link></li>     
            <li><Link to='/formclass'>Form Class</Link></li>     
            <li><Link to='/news'>News</Link></li>     
            
        </ul>

        {props.children}
    </>
  )
}

export default BaseLayout
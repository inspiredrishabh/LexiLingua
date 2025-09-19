import React from 'react'
import './App.css'
import LexiLinguaHomepage from './components/LexiLinguaHomepage'
import LexiLinguaDemo from './components/LexiLinguaDemo'
import LexiLinguaUpload from './components/LexiLinguaUpload'

function App() {
  // Simple routing based on URL path
  const path = window.location.pathname;
  
  if (path === '/demo') {
    return <LexiLinguaDemo />
  }
  
  if (path === '/upload') {
    return <LexiLinguaUpload />
  }
  
  return <LexiLinguaHomepage />
}

export default App

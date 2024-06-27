import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { motion } from "framer-motion";
import TextAnim from './TextAnim';
import Hero from './hero';
import Intro1 from './Intro1';
import Intro2 from './intro2';
// import Recommended from './Recommended';
import footer from './assets/footer.svg'
import Authentication from './authentication';
import Success from './success';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Hero />
      <Intro1 />
      <Intro2 />
      <img src={footer} className='max-w-[1024px]'/>
      {/* <Success /> */}
    </>
  )
}

export default App

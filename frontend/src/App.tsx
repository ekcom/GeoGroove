import './App.css'
import Hero from './hero';
import Intro1 from './Intro1';
import Intro2 from './intro2';
import footer from './assets/footer.svg'

function App() {

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

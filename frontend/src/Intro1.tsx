import image from './assets/intro1.svg';
import note1 from './assets/note1.svg';

export default function Intro1() {
  return (
    <section className='max-w-[1024px] bg-[#1F1F1F] flex flex-row gap-5 relative mt-80 py-12'>
      <img src={note1} className='absolute -top-40' />
      <div className='ml-20 z-10'>
        <div className='text-4xl font-bold my-10 text-left ml-60'>
          Discover new music as you explore.
        </div>
        <div className='text-2xl text-justify mr-20'>
          Miami? Chicago? New York? Yes you can add all of those destinations. Whether it be the classic 90’s tunes or mega blockbuster songs, the world’s music library is at your fingertips. 
        </div>
      </div>
      <img src={image}></img>
    </section>
  )
}
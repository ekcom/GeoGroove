import image from './assets/intro2.svg';
import note2 from './assets/note2.svg';

export default function Intro2() {
  return (
    <section className='max-w-[1024px] bg-[#1F1F1F] flex flex-row gap-5 relative mt-60 py-12'>
      <img src={note2} className='absolute -top-40' />
      <div className='ml-20 z-10'>
        <div className='text-4xl font-bold my-10 text-left ml-60'>
        Create your custom playlist in Spotify.
        </div>
        <div className='text-2xl text-justify mr-20'>
            You can see your customized playlist in Spotify. All the top artists in the area. All the top songs from those artists. Immerse yourself in the cultural fabric of your area.
        </div>
      </div>
      <img src={image}></img>
    </section>
  )
}
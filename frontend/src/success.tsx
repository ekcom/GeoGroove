import spotify from './assets/spotify.svg'
import success from './assets/success.svg'

export default function Success() {

    const view = () => {

    }
    return (
        <section className='flex flex-col items-center'>
            <div className="text-6xl font-bold mb-20">
                Playlist uploaded!
            </div>
            <img src={success} />
            <div className='text-4xl'>
                You have successfully linked to Spotify. 
                Click on the button below to view your playlist.
            </div>
            <button className="px-8 py-4 text-4xl font-bold bg-[#329E01] rounded-full mt-10" onClick={view}>
                View Playlist{' '}
                <img src={spotify} className='inline'/>
            </button>
        </section>
    )
}
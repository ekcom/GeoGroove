import spotify from './assets/spotify.svg'

export default function Authentication() {

    const authenticate = () => {

    }
    return (
        <section>
            <div className="text-6xl font-bold mb-40">
                Authenticate with Spotify.
            </div>
            <button className="px-8 py-4 text-4xl font-bold bg-[#329E01] rounded-full" onClick={authenticate}>
                Authenticate{' '}
                <img src={spotify} className='inline'/>
            </button>
        </section>
    )
}
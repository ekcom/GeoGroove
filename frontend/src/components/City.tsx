export default function City(props: {cityName: string, color: string, addCity: (city: string) => void}) {

  const colorStyle: React.CSSProperties = {
    backgroundColor: props.color
  };

  return (
    <button className="text-3xl font-bold pt-3 px-5 rounded-3xl bg-pink-700 border-0 outline-none" style={colorStyle} onClick={() => props.addCity(props.cityName)}>
      {props.cityName} +
    </button>
  )
}
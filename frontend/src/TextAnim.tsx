import { motion, useMotionValue, useTransform, animate } from "framer-motion";
import { useEffect } from "react";
import CursorBlinker from "./CursorBlinker";


export default function TextAnim() {
  const baseText = "Find local artists with GeoGroove." as string;
  const count = useMotionValue(0);
  const rounded = useTransform(count, (latest) => Math.round(latest));
  const displayText = useTransform(rounded, (latest) =>
    baseText.slice(0, latest)
  );

  useEffect(() => {
    const controls = animate(count, baseText.length, {
      type: "tween",
      duration: 3,
      ease: "easeInOut",
    });
    return controls.stop;
  }, []);

  return (
    <div className="text-2xl font-bold text-left">
      <motion.h1 className="inline">{displayText}</motion.h1>
      <CursorBlinker />
    </div>
  );
}

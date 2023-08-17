import React, { useState } from "react";

interface TooltipProps {
  children: React.ReactNode;
  content: React.ReactNode;
  direction?: "top" | "right" | "bottom" | "left";
  delay?: number;
}

const Tooltip: React.FC<TooltipProps> = (props) => {
  let timeout: ReturnType<typeof setTimeout>;
  const [active, setActive] = useState(false);

  const showTip = () => {
    timeout = setTimeout(() => {
      setActive(true);
    }, props.delay || 400);
  };

  const hideTip = () => {
    clearTimeout(timeout);
    setActive(false);
  };

  return (
    <div
      className={`relative inline-block ${active ? "" : "group"}`}
      onMouseEnter={showTip}
      onMouseLeave={hideTip}
    >
      {props.children}
      {active && (
        <div
          className={`absolute bg-black text-white px-6 py-2 text-sm font-sans rounded z-10 ${
            props.direction === "right" ? "left-full top-1/2 transform -translate-y-1/2" :
            props.direction === "bottom" ? "bottom-full" :
            props.direction === "left" ? "right-full top-1/2 transform -translate-y-1/2" :
            "top-full"
          }`}
        >
          {props.content}
          <div
            className={`absolute ${
              props.direction === "right" ? "left-full ml-2 border-l border-black border-solid" :
              props.direction === "bottom" ? "top-full mt-2 border-t border-black border-solid" :
              props.direction === "left" ? "right-full mr-2 border-r border-black border-solid" :
              "bottom-full mb-2 border-b border-black border-solid"
            }`}
          ></div>
        </div>
      )}
    </div>
  );
};

export default Tooltip;

import React from "react";
import Image from "next/image";
import { LoaderPinwheel } from "lucide-react";
export function Loader() {
  return (
    <div className="h-full flex flex-col gap-y-4 items-center justify-center">
      <div className="w-10 h-10 relative animate-spin">
        <LoaderPinwheel className="text-black" />
      </div>
      <p className="text-sm text-muted-foreground">Processing...</p>
    </div>
  );
}
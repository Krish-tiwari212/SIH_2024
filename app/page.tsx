import Image from "next/image";
import { Button } from "@/components/ui/button";
import Sidebar from "@/components/sidebar";
import { redirect } from 'next/navigation';

export default function Home() {
  redirect("/dashboard");
  return (
    <main className="h-screen">
      <div className="hidden h-full md:flex md:w-72 md:flex-col md:fixed md:inset-y-0 bg-gray-900">
        <Sidebar/>
      </div>
      <Button variant="outline" className="text-white bg-slate-900">
        Hello
      </Button>
    </main>
  );
}

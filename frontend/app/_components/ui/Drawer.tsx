"use client";
import { Button } from "@/components/ui/button";
import { Drawer, DrawerContent, DrawerHeader, DrawerTitle, DrawerDescription, DrawerClose } from "@/components/ui/drawer";
import { X } from "@mynaui/icons-react";
interface DrawerProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;
}


export default function DrawerComponent({ open, onOpenChange }: DrawerProps) {
    return (
         <Drawer open={open} onOpenChange={onOpenChange} direction="left">
            <DrawerContent>
                <DrawerHeader>
                    <div className="flex flex-row w-full  items-center justify-between">
                        <DrawerTitle>Welcome User</DrawerTitle>
                        <DrawerClose asChild><Button variant="outline" className="rounded-md border-none"><X/></Button></DrawerClose>
                    </div>
                    <DrawerDescription>bla bla bla bla la</DrawerDescription>
                </DrawerHeader>
            </DrawerContent>

        </Drawer>
           ) 
    
}
"use client"
import { PanelLeft } from "@mynaui/icons-react";
import React from 'react';
import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ChartContainer } from "@/components/ui/chart";
import Drawer from '../_components/ui/Drawer';
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";

export default function DashboardPage() {

    const [isOpen, setIsOpen] = useState(false);

    return (
        <>
            <Drawer open={isOpen} onOpenChange={() => setIsOpen(!isOpen)}></Drawer>
            <div className="flex justify-between items-center">
                <div className="p-3 flex items-center">
                    <Button variant="outline" className="border-none rounded-md mx-2" onClick={() => setIsOpen(!isOpen)}><PanelLeft /></Button>
                    <h1>Last Applications</h1>
                </div>
                <div className="p-3 flex items-center">
                    <Avatar size="lg">
                        CN
                    </Avatar>
                </div>
            </div>
            <main>
                <section id="application-chart">

                </section>
            </main>

        </>
    );
}
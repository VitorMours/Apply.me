"use client";

import { Bubble, BubbleContent } from "@/components/ui/bubble";
import { Input } from "@/components/ui/input";
import { Message, MessageContent } from "@/components/ui/message";


export default function ChatPage() {
    return(
    <div className="p-10 flex w-3/4 flex-col center h-screen">
        <Message>
            <MessageContent>
                <Bubble variant="muted">
                    <BubbleContent className="rounded-md mb-3">
                        Olá, como posso ajudá-lo hoje?
                    </BubbleContent>
                </Bubble>
            </MessageContent>
        </Message>
        <Input className="rounded-md" />   
    </div>
    );
}
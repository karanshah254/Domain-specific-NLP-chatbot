import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';
import { MatDividerModule } from '@angular/material/divider';
import { ChatService } from '../services/chat.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [
    FormsModule,
    CommonModule,
    MatCardModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    MatToolbarModule,
    MatListModule,
    MatDividerModule,
    HttpClientModule,
  ],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css',
})
export class ChatComponent implements OnInit {
  userMessage: string = '';
  messages: any[] = [];
  isLoading: boolean = false;

  constructor(private chatService: ChatService) {}

  ngOnInit(): void {

  const savedChat = localStorage.getItem('vgecChatHistory');

  if (savedChat) {
    this.messages = JSON.parse(savedChat);
  } else {
    this.messages.push({
      sender: 'bot',
      text: `
        👋 Welcome to <b>VGEC Intelligent Assistant</b>! <br><br>
        I can help you with:
        <ul style="margin:5px 0 5px 15px;">
          <li>Admissions</li>
          <li>Fee Structure</li>
          <li>Courses Offered</li>
          <li>Placements</li>
          <li>Hostel & Facilities</li>
        </ul>
        For more visit: <a href="https://www.vgecg.ac.in/" target="_blank">VGEC Official Website</a>
      `
    });
  }

  setTimeout(() => this.scrollToBottom(), 100);
}

  sendMessage() {
    if (!this.userMessage.trim()) return;

    const userText = this.userMessage;

    this.messages.push({ sender: 'user', text: userText });
    localStorage.setItem('vgecChatHistory', JSON.stringify(this.messages));

    this.userMessage = '';
    this.isLoading = true;

    this.chatService.sendMessage(userText).subscribe({
      next: (response) => {
        setTimeout(() => {
          this.isLoading = false;

          this.messages.push({
            sender: 'bot',
            text: response.response,
          });
          localStorage.setItem('vgecChatHistory', JSON.stringify(this.messages));

          this.scrollToBottom();
        }, 700); // 👈 Typing visible for 700ms
      },
      error: (err) => {
        this.isLoading = false;
        this.messages.push({
          sender: 'bot',
          text: 'Server error. Please try again.',
        });
        localStorage.setItem('vgecChatHistory', JSON.stringify(this.messages));

        setTimeout(() => this.scrollToBottom(), 100);
      },
    });
  }

  scrollToBottom() {
    const chatBox = document.querySelector('.chat-box');
    if (chatBox) {
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  }
}

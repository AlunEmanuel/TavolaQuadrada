import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ItemService, Item } from './services/item';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrls: ['./app.scss']
})
export class AppComponent {
  title = 'TavolaQuadrada App';
  items: Item[] = [];
  newItem: Item = { name: '', description: '' };

  constructor(private itemService: ItemService) {
    this.loadItems();
  }

  loadItems() {
    this.itemService.getItems().subscribe(items => this.items = items);
  }

  createItem() {
    if (!this.newItem.name || !this.newItem.description) return;
    this.itemService.createItem(this.newItem).subscribe(item => {
      this.items.push(item);
      this.newItem = { name: '', description: '' };
    });
  }
}

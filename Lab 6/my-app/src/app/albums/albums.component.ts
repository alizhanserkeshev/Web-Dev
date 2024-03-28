import { Component } from '@angular/core';
import { Album } from '../album';
import { AlbumsService } from '../albums.service';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent {
  albums!: Album[];

  constructor(private albumService: AlbumsService){}

  ngOnInit(){
    this.albumService.getAlbums().subscribe((albums) => {
      this.albums = albums.slice(0, 10);
    })
  }

  deleteAlbum(id: number){
    this.albums = this.albums.filter(a => a.id !== id)
  }
}

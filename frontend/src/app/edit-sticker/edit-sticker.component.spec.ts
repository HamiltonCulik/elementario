import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewStickerComponent } from './new-sticker.component';

describe('NewStickerComponent', () => {
  let component: NewStickerComponent;
  let fixture: ComponentFixture<NewStickerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewStickerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewStickerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

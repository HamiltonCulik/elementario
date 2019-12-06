import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowMapsComponent } from './show-maps.component';

describe('ShowMapsComponent', () => {
  let component: ShowMapsComponent;
  let fixture: ComponentFixture<ShowMapsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ShowMapsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ShowMapsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { Component, OnInit } from '@angular/core';
import {FilterItemComponent} from "../filter-item/filter-item.component";
import { HttpClient } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';



@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.css']
})
export class FilterComponent implements OnInit {
  filter_number = [0];

  data = {
      'Models': ['Audi', 'Green', '2001'],
      'Color':["red"],
      'Year':[1234, 2345]
  };
  columns = [];
  value = [];

  result_params = {
    'Columns': [],
    'Operators': [],
    'Values': [],
    'Btw_operators': [],
  };

  constructor( private http: HttpClient) { }

  ngOnInit() {
    this.columns = Object.keys(this.data);
    this.value = this.data["Models"];
  }

  addElement(): void {
  this.filter_number.push(this.filter_number.length);
}

  getUser() {
    return this.http.get(`https://conduit.productionready.io/api/profiles/eric`)
    .map((res:Response) => res.json());
  }

  pushParams(data){
    this.result_params.Columns.push(data.column);
    this.result_params.Operators.push(data.operator);
    this.result_params.Values.push(data.value);
    this.result_params.Btw_operators.push(data.btw_elem_operator);
    console.log(this.result_params)
  }

}

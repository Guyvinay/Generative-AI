import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { RegistrationService } from './registration.service';
import { HttpClient } from '@angular/common/http';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  // registrationForm !: FormGroup;

  successMessage: string | null = null;
  failureMessage: string | null = null;


  user = {
    name: '',
    email: '',
    password: '',
    address:'',
    role:''
  };

  // constructor(
  //   private formBuilder: FormBuilder,
  //   private registrationService: RegistrationService
  // ) {
  //   this.registrationForm = this.formBuilder.group({
  //     name: ['', Validators.required],
  //     email: ['', [Validators.required, Validators.email]],
  //     password: ['', [Validators.required, Validators.minLength(6)]],
  //     // Add other registration fields here
  //   });
  // }

  constructor(
    private http: HttpClient,
    private toastr : ToastrService,
    private router : Router,
    ) {}


  onSubmit(): void {
   const registrationData = {
    name : this.user.name,
    email:this.user.email,
    password:this.user.password,
    address:this.user.address,
    role:this.user.role
   }
   this.http.post(
    'http://localhost:8080/customers' , 
    registrationData
   )
   .subscribe(
    (response) => {
      this.successMessage = 'Registration Successfull!';
      this.failureMessage = null;
      // this.toastr.success('Registration successful!', 'Success', { timeOut: 3000 });
      console.log('Registration Successfull',response);

      setTimeout(()=>{
        this.router.navigate(['/dashboard']);
      },2000);

    },
    (error)=>{
      this.failureMessage = 'Registration Failed';
      // this.toastr.error('Registration failed. Please try again.', 'Error', { timeOut: 3000 }); // Show error toast
      this.successMessage = null;
      console.log('Registration Failed: ', error)
    }
   )

  }
}

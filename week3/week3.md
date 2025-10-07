1. ES2015+


<1-1. const, let>
- 변수 선언은 const와 let을 사용한다

if (true) {
  var x=3;
  }
  console.log(x);  //3
  
  if (true) {
    const y=3;
    }
    console.log(y);  //Uncaught ReferenceError: y is not defined

- var은 함수 스코프를 가지므로 if문의 블록과 관계없이 접근할 수 있다
- 그러나 const와 let은 블록 스코프를 가지므로 블록 밖에서는 접근할 수 없다


const a = 0;
a = 1; // Uncaught TypeError : Assignment to constant variable

let b = 0;
b = 1;  // 1

- const는 한 번 값을 할당하면 다른 값을 할당할 수 없다
- 따라서 const로 선언한 변수를 상수라고 부르기도 한다





<1-2. 템플릿 문자열>
const num3 = 1;
const num4 = 2;
const result2 = 3;

console.log(`${num3} 더하기 ${num4}는 ' ${result2}'`);  // 1 더하기 2는 '3'
- ${ 변수 } 형식으로 더하기 기호 없이 문자열을 넣을 수 있다
- 기존 따옴표 대신 백틱을 사용하므로 큰따옴표나 작은따옴표와 함께 사용할 수도 있다





<1-3. 객체 리터널>
var sayNode = function() {
  console.log('Node');
};
var es = 'ES';
var oldObject = {
  sayJS: function() {
    console.log('JS');
  },
  sayNode: sayNode,
};
oldObject[es + 6] = 'Fantastic';
oldObject.sayNode(); // Node
oldObject.sayJS(); // JS
console.log(oldObject.ES6); // Fantastic
const newObject = {
  sayJS() {
    console.log('JS');
  },
  sayNode,
  [es + 6]: 'Fantastic',
};
newObject.sayNode(); // Node
newObject.sayJS(); // JS
console.log(newObject.ES6); // Fantastic

- 객체의 메서드에 함수를 연결할 때, 콜론(:)과 function을 붙이지 않아도 된다
- 속성명과 변수명이 동일한 경우 한 번만 써도 된다
- 객체 리터럴 안에서 동적 속성을 선언해도 된다
  > 위의 코드를 보면 newObject안에 [es+6]이 속성명으로 바로 사용되고 있음





<1-4. 화살표 함수>
function add1(x, y) {
  return x + y;
}

const add2 = (x, y) => {
  return x + y;
};

const add3 = (x, y) => x + y;

const add4 = (x, y) => (x + y);

function not1(x) {
  return !x;
}

const not2 = x => !x;

- function 대신 => 기호로 함수를 선언할 수 있다
- 변수에 대입하여 재사용할 수 있다
- 내부에 return문 밖에 없는 경우, return 키워드와 중괄호를 생략할 수 있다
- 매개변수가 한 개이면 소괄호를 생략할 수 있다





<1-5. 클래스>
class Human {
    constructor(type = 'human') {
      this.type = type;
    }
  
    static isHuman(human) {
      return human instanceof Human;
    }
  
    breathe() {
      alert('h-a-a-a-m');
    }
  }
  
  class Zero extends Human {
    constructor(type, firstName, lastName) {
      super(type);
      this.firstName = firstName;
      this.lastName = lastName;
    }
  
    sayName() {
      super.breathe();
      alert(`${this.firstName} ${this.lastName}`);
    }
  }
  
  const newZero = new Zero('human', 'Zero', 'Cho');
  Human.isHuman(newZero); // true

- 클래스 문법이 추가되었지만, 여전히 프로토타입 기반으로 동작한다
  > 프로토타입 기반 문법을 보기 좋게 클래스로 바꾼 것





<1-6. 프로미스>
1) Promise 란?

const condition = true; // true이면 resolve, false이면 reject
const promise = new Promise((resolve, reject) => {
  if (condition) {
    resolve('성공');
  } else {
    reject('실패');
  }
});
// 다른 코드가 들어갈 수 있음
promise
  .then((message) => {
    console.log(message); // 성공(resolve)한 경우 실행
  })
  .catch((error) => {
    console.error(error); // 실패(reject)한 경우 실행
  })
  .finally(() => { // 끝나고 무조건 실행
    console.log('무조건');
});

- new Promise로 프로미스를 생성할 수 있으며, resolve, reject를 매개변수로 갖는 콜백 함수를 넣는다
- 만들어진 promise 변수에 then, catch 메서드를 붙일 수 있다
- 프로미스 내부에서 resolve가 호출되면 then이 실행되고, reject가 호출되면 catch가 실행된다
- finally 부분은 성공/실패 여부와 상관없이 실행된다
- Promise는 실행은 바로 하되, 결괏값은 나중에 받는 객체이다
  > 결괏값은 실행이 완료된 후, then이나 catch 메서드를 통해 받는다



2) 여러 개의 then이나 catch 사용 가능

promise
  .then((message) => {
    return new Promise((resolve, reject) => {
      resolve(message);
    });
  })
  .then((message2) => {
    console.log(message2);
    return new Promise((resolve, reject) => {
      resolve(message2);
    });
  })
  .then((message3) => {
    console.log(message3);
  })

  .catch((error) => {
    console.error(error);
});

- then이나 catch에서 다시 다른 then이나 catch를 붙일 수도 있다.
  > 이전 then의 return 값을 다음 then의 매개변수로 가진다
- 프로미스를 return한 경우, 프로미스가 수행된 후 다음 then이나 catch가 호출된다
- 단, then에서 new Promise를 return 해야 다음 then에서 받을 수 있다.



3) 콜백 함수

function findAndSaveUser(Users) {
      Users.findOne({})
        .then((user) => {
          user.name = 'zero';
          return user.save();
        })
        .then((user) => {
          return Users.findOne({ gender: 'm' });
        })
        .then((user) => {
          // 생략
        })
        .catch(err => {
          console.error(err);
        });
    }

- 프로미스는 콜백이 여러 번 중첩되는 문제를 해결할 수 있다. 
  > 단, 메서드가 내부적으로 프로미스 객체를 가지고 있는 경우에만 사용할 수 있다



4) 여러 개의 프로미스를 한 번에 실행 (promise.all)

const promise1 = Promise.resolve('성공1');
const promise2 = Promise.resolve('성공2');
Promise.all([promise1, promise2])
  .then((result) => {
    console.log(result); // ['성공1', '성공2'];
  })
  .catch((error) => {
    console.error(error);
  });

- Promise.resolve: 즉시 resolve하는 프로미스를 만드는 방법
-  Promise.reject: 즉시 reject하는 프로미스를 만드는 방법
- Promise.all : 프로미스 여러 개를 한 번에 실행시키는 방법
  > 프로미스 중 하나라도 reject 되면 catch로 넘어간다
- Promise.allSettled : status를 통해 어떤 프로미스가 reject 되었는지 알아낼 수 있는 방법
-  reject된 Promise에 catch를 달지 않으면 에러가 발생하므로, 반드시 catch 메서드를 붙이는 것을 권장
  > 에러가 발생하면  다음 코드 실행 불가





<1-7. async / await>
- 프로미스를 사용한 코드를 한 번 더 깔끔하게 줄일 수 있다

function findAndSaveUser(Users) {
  Users.findOne({})
    .then((user) => {
      user.name = 'zero';
      return user.save();
    })
    .then((user) => {
      return Users.findOne({ gender: 'm' });
    })
    .then((user) => {
      // 생략
    })
    .catch(err => {
      console.error(err);
     });
    }


// 일반 함수 대신 async funtion으로 함수 선언
async function findAndSaveUser(Users) {
    try {
// 프로미스 앞에 await -> 프로미스가 resolve될 때까지 기다린 뒤 다음 로직으로 넘어감
        let user = await Users.findOne({});
        user.name = 'zero';
        user = await user.save();
        user = await Users.findOne({gender : 'm'});
        // 생략
    }
    catch (error) {
        console.error(error);
    }
}


// 화살표 함수도 사용 가능
const findAndSaveUser = async (Users) => {
  try {
    let user = await Users.findOne({});
    user.name = 'zero';
    user = await user.save();
    user = await Users.findOne({ gender: 'm' });
    // 생략
  } catch (error) {
    console.error(error);
  }
};
const promise1 = Promise.resolve('성공1');
const promise2 = Promise.resolve('성공2');
(async () => {
// for await문을 사용하여 프로미스 배열을 순회
  for await (promise of [promise1, promise2]) {
    console.log(promise);
  }
})();




<1-8. Map / Set>
- Map은 객체와 유사하고, Set은 배열과 유사하다

const m = new Map();

m.set('a', 'b'); // set(키, 값)으로 Map에 속성 추가
m.set(3, 'c'); // 문자열이 아닌 값을 키로 사용 가능합니다
const d = {};
m.set(d, 'e'); // 객체도 됩니다

m.get(d); // get(키)로 속성값 조회
console.log(m.get(d)); // e

m.size; // size로 속성 개수 조회
console.log(m.size) // 3

for (const [k, v] of m) { // 반복문에 바로 넣어 사용 가능합니다
  console.log(k, v); // 'a', 'b', 3, 'c', {}, 'e'
} // 속성 간의 순서도 보장됩니다

m.forEach((v, k) => { // forEach도 사용 가능합니다
  console.log(k, v); // 결과는 위와 동일
});

m.has(d); // has(키)로 속성 존재 여부를 확인합니다
console.log(m.has(d)); // true

m.delete(d); // delete(키)로 속성을 삭제합니다
m.clear(); // clear()로 전부 제거합니다
console.log(m.size); // 0

- Map은 속성들 간의 순서를 보장하고, 반복문을 사용할 수 있다
- 그러나 속성명으로 문자열이 아닌 값도 사용할 수 있고,
- size 메서드를 통해 속성의 수를 쉽게 알 수 있다는 점에서 일반 객체와 다름



const s = new Set();
s.add(false); // add(요소)로 Set에 추가합니다
s.add(1);
s.add('1');
s.add(1); // 중복이므로 무시됩니다
s.add(2);

console.log(s.size); // 중복이 제거되어 4

s.has(1); // has(요소)로 요소 존재 여부를 확인합니다
console.log(s.has(1)); // true

for (const a of s) {
  console.log(a); // false 1 '1' 2
}

s.forEach((a) => {
  console.log(a); // false 1 '1' 2
})

s.delete(2); // delete(요소)로 요소를 제거합니다
s.clear(); // clear()로 전부 제거합니다
- Set은 중복을 허용하지 않는다
  > 배열 자료구조를 사용하고 싶으나, 중복을 허용하고 싶지 않을 때 사용
  > 기존 배열에서 중복을 제거하고 싶을 때에도 사용
- new Set(배열) : 배열의 중복 제거
- Array.from(Set) : Set을 배열로 되돌림





<1-9. 널 병합 / 옵셔널 체이닝>
const c = 0;
const d = c ?? 3; // ?? 연산자는 null과 undefined일 때만 뒤로 넘어감
console.log(d); // 0;

const e = null;
const f = e ?? 3;
console.log(f); // 3;

const g = undefined;
const h = g ?? 3;
console.log(h); // 3;

- 널 병합 연산자는 주로 || 연산자 대용으로 사용된다
- falsy 값(0, '', false, NaN, null, undefined) 중 null과 undefined만 따로 구분한다



const a = {}
a.b; // a가 객체이므로 문제없음

const c = null;
try {
  c.d;
} catch (e) {
  console.error(e); // TypeError: Cannot read properties of null (reading 'd')
}
c?.d; // 문제없음

try {
  c.f();
} catch (e) {
  console.error(e); // TypeError: Cannot read properties of null (reading 'f')
}
c?.f(); // 문제없음

try {
  c[0];
} catch (e) {
  console.error(e); // TypeError: Cannot read properties of null (reading '0')
}
c?.[0]; // 문제없음

- 옵셔널 체이닝 연산자는 null이나 undefined의 속성을 조회하는 경우, 에러가 발생하는 것을 막는다
- 일반적인 속성뿐만 아니라 함수 호출이나 배열 요소 접근에 대해서도 에러가 발생하는 것을 방지할 수 있다
- c?, .d, c?.f(), c?.[0]의 값은 undefined이다





2. 프런트엔드 자바스크립트


<2-1. AJAX>
- 비동기적 웹 서비스를 개발할 때 사용하는 기법
- 페이지 이동 없이 서버에 요청을 보내고 응답을 받는 기술



1) GET 요청

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<script>
	(async () => {
    	try {
        	const result = await axios.get('https://www.zerocho.com/api/get');
    		console.log(result);
    		console.log(result.data); // {}
  		} catch (error) {
    		console.error(error);
  		}
	})();
</script>

- axios.get 내부에도 new Promise가 들어있기 때문에, then과 catch를 사용할 수 있다
- result.data에 서버로부터 보낸 데이터가 들어있으며, 개발자 도구 Console 탭에서 확인할 수 있다



2) POST 요청

(async () => {
  try {
    const result = await axios.post('https://www.zerocho.com/api/post/json', {
      name: 'zerocho',
      birth: 1994,
    });
    console.log(result);
    console.log(result.data);
  } catch (error) {
    console.error(error);
  }
})();

- axios.post 함수의 두 번째 인수로 데이터를 넣어 보낸다





<2-2. Form Data>
- HTML form 태그의 데이터를 동적으로 제어할 수 있는 기능
- 주로 AJAX와 함께 사용


1) FormData 생성자로 객체 생성

const formData = new FormData();
//append 메서드: 키-값 형식의 데이터 저장, 키 하나에 여러 개의 값 추가 가능
formData.append('name', 'zerocho'); 
formData.append('item', 'orange');
formData.append('item', 'melon');
//has 메서드: 주어진 키에 해당하는 값이 있는지 여부
formData.has('item'); // true;
formData.has('money'); // false;
//get 메서드: 주어진 키에 해당하는 값 하나를 가져옴
formData.get('item');// orange
//getAll 메서드: 해당하는 모든 값을 가져옴
formData.getAll('item'); // ['orange', 'melon'];
formData.append('test', ['hi', 'zero']);
formData.get('test'); // hi, zero
//delete 메서드: 현재 키를 제거
formData.delete('test');
formData.get('test'); // null
//set 메서드: 현재 키를 수정
formData.set('item', 'apple');
formData.getAll('item'); // ['apple'];

- 생성된 객체의 append 메서드로 키-값 형식의 데이터를 저장할 수 있다
- append 메서드를 여러 번 사용해서 키 하나에 여러 개의 값을 추가해도 된다
- has : 주어진 키에 해당 값이 있는지 여부를 알림
- get : 주어진 키에 해당하는 값 하나를 가져옴
- getAll : 해당하는 값 모두를 가져옴
- delete : 현재 키를 제거
- set : 현재 키를 수정



2) axios로 폼 데이터를 서버로 보냄

(async () => {
  try {
    const formData = new FormData();
    formData.append('name', 'zerocho');
    formData.append('birth', 1994);
    const result = await axios.post('https://www.zerocho.com/api/post/formdata', formData);
    console.log(result);
    console.log(result.data);
  } catch (error) {
    console.error(error);
  }
})();

- 두 번째 인수에 데이터를 넣어 보낸다





<2-3. encodeURIComponent, decodeURIComponent>
(async () => {
  try {
    const result = await axios.get(`https://www.zerocho.com/api/search/${encodeURIComponent('노드')}`);
    console.log(result);  
    console.log(result.data); // {}
  } catch (error) {
    console.error(error);
  }
})();

- AJAX 요청을 보낼 때, 주소에 한글이 들어가는 경우 사용
   > 한글 주소를 문자열로 변환
   > 한글 부분만 encodeURIComponent 메서드로 감싼다
  > 받는 쪽에서는 decodeURIComponent를 사용하면 된다
- 브라우저뿐만 아니라,  노드에서도 사용 가능





2-4. 데이터 속성과 dataset
- 데이터 속성: 보안과 관련 없는 데이터들을 HTML과 관련된 데이터에 저장하는 공식적인 방법

<ul>
<li data-id="1" data-user-job="programmer">Zero</li>
  <li data-id="2" data-user-job="designer">Nero</li>
  <li data-id="3" data-user-job="programmer">Hero</li>
  <li data-id="4" data-user-job="ceo">Kero</li>
</ul>
<script>
  console.log(document.querySelector('li').dataset);
  //dataset 속성을 통해 첫 번째 li 태그의 데이터 속성에 접근
  // { id: '1', userJob: 'programmer' } (데이터 속성의 이름이 조금씩 변형됨)
</script>

- HTML 태그의 속성으로 data-로 시작하는 것들이 데이터 속성이다
- 자바스크립트로 쉽게 접근 가능하다




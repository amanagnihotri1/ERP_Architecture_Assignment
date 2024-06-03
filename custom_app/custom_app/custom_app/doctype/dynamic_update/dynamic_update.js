// Copyright (c) 2024, Aman and contributors
// For license information, please see license.txt
frappe.ui.form.on('dynamic_update', {
      before_save(frm) {
          if (!frm.doc.table2) {
              frm.doc.table2 = [];
          }
          if (!frm.doc.table1) {
              frm.doc.table1 = [];
          }
          frm.doc.row_count=parseInt(frm.doc.table1.length||frm.doc.table2.length);
          if (!frm.doc.table2) {
              frm.doc.table2 = [];
          }
          if (!frm.doc.table1) {
              frm.doc.table1 = [];
          }
  },
});
  frappe.ui.form.on('enrolledStudents', {
      first_name: function(frm, cdt, cdn) {
          table_manipulate(frm, cdt, cdn,'table2');
      },
      last_name: function(frm, cdt, cdn) {
          table_manipulate(frm, cdt, cdn,'table2');
      },
      age:function(frm, cdt, cdn) {
         table_manipulate(frm, cdt, cdn,'table2');
      },
      before_table1_remove: function(frm, cdt, cdn) {
          var target_row_index = locals[cdt][cdn].idx;
          if (frm.doc.table2 && frm.doc.table2.length >= target_row_index&&target_row_index>0) {
              frm.get_field('table2').grid.grid_rows[target_row_index - 1].remove();
              frm.refresh_field('table2');
          } else {
                  console.log("Target row not found in table2:", target_row_index);
          }
      }
  });
  
  frappe.ui.form.on('student_info', {
      form_render: function(frm, cdt, cdn) {
          table_manipulate(frm, cdt, cdn,'table1');
      },
      first_name: function(frm, cdt, cdn) {
         table_manipulate(frm, cdt, cdn,'table1');
      },
      last_name: function(frm, cdt, cdn) {
          table_manipulate(frm, cdt, cdn,'table1');
      },
      age: function(frm, cdt, cdn) {
          table_manipulate(frm, cdt, cdn,'table1');
      },
      before_t2_remove: function(frm, cdt, cdn) {
          var target_row_index = locals[cdt][cdn].idx;
          if (frm.doc.table2 && frm.doc.table2.length >= target_row_index&&target_row_index>0) {
              frm.get_field('table1').grid.grid_rows[target_row_index - 1].remove();
              frm.refresh_field('table1');
          } else {
              console.log("Target row not found in table2:", target_row_index);
          }
      }
  });
  
function table_manipulate(frm, cdt, cdn, target_table) {
      let row = locals[cdt][cdn];
      let sec_row;
      if (!frm.doc[target_table]) {
          frm.doc[target_table] = [];
      }
      sec_row = frm.doc[target_table].find(d => d.idx === row.idx);
  
      if (!sec_row) {
          sec_row = frm.add_child(target_table);
          sec_row.idx = row.idx; 
      }
      sec_row.first_name = row.first_name;
      sec_row.last_name = row.last_name;
      sec_row.age = row.age;
      sec_row.contact=row.contact;
  
      frm.refresh_field(target_table);
  }
  
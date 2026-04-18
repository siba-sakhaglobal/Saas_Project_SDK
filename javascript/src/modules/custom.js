/**
 * Custom module — dynamic CRUD for any SurrealDB-backed table.
 * Usage: cms.custom('reviews').list({ page: 1 })
 */

export class CustomModule {
  constructor(client, table) {
    this.c = client;
    this.table = table;
  }

  list(params) { return this.c.get(`/api/custom/${this.table}`, { params }); }
  get(id) { return this.c.get(`/api/custom/${this.table}/${id}`); }
  create(body) { return this.c.post(`/api/custom/${this.table}`, body); }
  update(id, body) { return this.c.put(`/api/custom/${this.table}/${id}`, body); }
  delete(id) { return this.c.delete(`/api/custom/${this.table}/${id}`); }
  count() { return this.c.get(`/api/custom/${this.table}/_count`); }
  query(sql, vars) { return this.c.post(`/api/custom/${this.table}/_query`, { sql, vars }); }
}

export class CustomModuleFactory {
  constructor(client) { this.c = client; }

  tables() { return this.c.get('/api/custom/_tables'); }

  module(table) { return new CustomModule(this.c, table); }
}
